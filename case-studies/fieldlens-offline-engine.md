# FieldLens Queue Repair & Validation 📱

## Status & Evidence

FieldLens is a mobile AI-coaching prototype for tradespeople. The earlier source review identified lost concurrent writes and retry counts. Those repairs are now implemented and merged; release readiness remains a separate question.

Public repository status checked on **9 October 2026**:

* **Merged:** [queue repair, PR #6](https://github.com/itsoumya-d/fieldlens__/pull/6), [shared sync handler, PR #7](https://github.com/itsoumya-d/fieldlens__/pull/7), [Expo SDK 55 runtime baseline, PR #8](https://github.com/itsoumya-d/fieldlens__/pull/8), and [browser voice restoration, PR #9](https://github.com/itsoumya-d/fieldlens__/pull/9).
* **Current main snapshot:** [`b035fc2`](https://github.com/itsoumya-d/fieldlens__/tree/b035fc284c1c8c93f20839af1f27b4bf68317bf3), containing those changes. PR #9 merged on 9 October 2026; that establishes source integration, not a release or deployment.

## The Failure and Repair

The [original implementation](https://github.com/itsoumya-d/fieldlens__/blob/72fb0fc9de033992d6ca7938a01c03eb9ce5188e/lib/offline.ts) independently read and rewrote the queue. Concurrent callers could overwrite each other's work, and a fresh final read discarded retry increments.

The merged [storage-only queue core](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/lib/offlineQueue.ts) serializes complete read/modify/write operations within one shared instance. After a remote attempt, it rereads the latest queue under the lock before persisting success or a retry. New enqueues and explicit removals survive. Overlapping sync calls share one pass.

A merged [dispatch factory](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/lib/offlineSync.ts) handles create, update and delete for both reconnect and banner entry points. Update/delete require a usable row ID; provider failures remain queued for retry. Storage failures reject instead of silently replacing unreadable work.

## Engineering Decision: Keep Network I/O Outside the Storage Lock

The [queue core](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/lib/offlineQueue.ts#L104-L139) locks the read/modify/write boundary, releases it for the remote handler, then rereads current storage under the lock to commit the result. A handler can enqueue new work while its request is pending; acknowledging the original item must preserve that work. An explicit removal must also stay removed.

This keeps same-runtime storage operations ordered without blocking them on network latency or holding the lock while a handler calls back into the queue. The pass uses an initial snapshot, so newly added work waits for the next pass. The trade-off is deliberately bounded: remote success and local acknowledgement are separate operations. An interrupted acknowledgement can cause another send, which requires a server-side idempotency contract to make safe. The tests expose that window rather than claiming exactly-once delivery.

## Reproducible Evidence

The [focused test guide](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/tests/README.md) documents `npm run test:offline` on Node 24 without provider credentials or dependency installation.

* PR #6 records a red/green comparison: 16 failures against the pre-fix algorithm, then all 23 queue cases passing with the repair.
* PR #7 adds dispatch and shared-wiring regressions, bringing the focused suite to 31 cases.
* Combined-main [offline CI](https://github.com/itsoumya-d/fieldlens__/actions/runs/37863471103) and [runtime CI](https://github.com/itsoumya-d/fieldlens__/actions/runs/37863471154) passed at `b035fc284c1c8c93f20839af1f27b4bf68317bf3`. These cover the provider-free queue/recorder/upload/Jest suites, app/helper typechecks and static web export. The separate [EAS build check](https://github.com/itsoumya-d/fieldlens__/actions/runs/37863471105) failed because Expo authentication was absent; no native build success is claimed.

Queue tests use JSON-backed in-memory storage and controlled promises. They exercise persisted retries across queue reconstruction, concurrent mutations, overlapping sync, malformed data and interrupted local acknowledgements. Recorder tests use fake browser boundaries and synthetic bytes. These results are tied to the referenced revisions, not a fresh test run performed for this case-study update.

## Remaining Boundaries

* The lock coordinates one queue instance in one JavaScript runtime. It does not coordinate browser tabs, processes or independently created instances.
* Remote success and local acknowledgement are not atomic. An interrupted acknowledgement can produce a repeated send; a regression explicitly demonstrates that window. Server-side idempotency, bounded retry/backoff and a recoverable dead-letter flow remain future work.
* Fake-client success does not establish affected rows, authorization or Supabase RLS correctness. Real AsyncStorage, device crash durability, account isolation and end-to-end reconnects remain unvalidated.
* The [merged runtime baseline](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/docs/runtime-baseline.md) documents the unresolved web biometric startup lock and dependency-security findings. A static export is not a demonstrated usable web app.
* The [merged browser-recorder notes](https://github.com/itsoumya-d/fieldlens__/blob/b035fc284c1c8c93f20839af1f27b4bf68317bf3/docs/web-voice-recording.md) describe stream cleanup and MIME handling, but actual browser permission/codec behavior, native devices and live transcription/provider behavior are unverified. No release or deployment is established by these checks.
