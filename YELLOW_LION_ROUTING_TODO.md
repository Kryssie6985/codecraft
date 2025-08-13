# Yellow Lion Routing TODO (No New Manager)

- Confirm orchestrator lion_id for Green Lion (default: "green-lion").
- Ensure Federation Station forwards `orchestrator.agent_task` to Green Lion and replies with `agent_task_result`.
- Register callbacks in UI/runtime:
  - on_agent_result → update logs/console and trigger follow-up actions.
- Exercise helpers:
  - request_manifest_weaver("route_plan", { scope: "voltron" })
  - request_audit_agent("federation_station", "deep")
- Optional: Add ephemeral correlation log map for pending tasks (in-memory).
- Do not add any new manager/orchestrator components.
