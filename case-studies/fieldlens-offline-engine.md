# FieldLens Offline Queue Source Review 📱

## Scope & Evidence

FieldLens is a mobile AI-coaching prototype for tradespeople. This note reviews its public offline queue and proposes reliability improvements. It does not claim that the proposed fixes have shipped.

* [Public repository](https://github.com/itsoumya-d/fieldlens__)
* [Reviewed implementation: lib/offline.ts](https://github.com/itsoumya-d/fieldlens__/blob/72fb0fc9de033992d6ca7938a01c03eb9ce5188e/lib/offline.ts)
* Reviewed revision: `72fb0fc9de033992d6ca7938a01c03eb9ce5188e`, on 8 October 2026

The module stores queued operations in AsyncStorage, checks connectivity and calls a supplied synchronization handler. It also includes cached reads and reconnect hooks.

## Findings From Source Inspection

### Concurrent read-modify-write operations

`enqueueOperation` reads the queue, appends an operation and writes the entire array. `dequeueOperation` follows a similar read/filter/write pattern. There is no shared serialization mechanism around these operations in the reviewed file.

Two callers can read the same earlier state and overwrite each other's changes. This is a source-level race analysis, not a recorded device-level reproduction.

### Retry metadata persistence

`processQueue` increments `retries` on objects in its initially loaded array. When a handler fails, the final persistence block calls `getQueue` again and writes that newly loaded array without merging the increments. The intended retry updates can therefore be lost.

### Missing recovery mechanisms

The reviewed queue does not implement the promise mutex, idempotency-key deduplication or dead-letter queue previously described in this case study. Those mechanisms belong in a proposed remediation plan until implemented and tested.

## Proposed Remediation

1. Serialize queue mutations within a clearly defined execution context. A JavaScript promise mutex can coordinate one runtime; it does not by itself guarantee cross-process or crash-safe transactions.
2. Persist retry metadata against the latest queue state without losing operations added while a handler is running.
3. Introduce stable operation identifiers and define server-side idempotency behavior before claiming duplicate-safe delivery.
4. Define bounded retries, backoff, a recoverable dead-letter state and a user-visible recovery path.
5. Specify how storage errors, malformed queue data, restarts and interrupted writes are handled.

## Verification Required Before Claiming a Fix

* Concurrent enqueue operations both remain persisted.
* Failed handlers persist retry counts across a reload.
* Processing and enqueueing concurrently do not discard new work.
* Duplicate delivery follows the documented idempotency contract.
* Exhausted retries can be inspected and recovered.
* Restart, storage-error and interrupted-write behavior is exercised.

No queue-specific test run or device test was performed for this documentation update. The previous five-test transcript is removed because it is not backed by a corresponding implementation and test file in the reviewed public revision.
