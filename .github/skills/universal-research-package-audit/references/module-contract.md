# Module contract

Each optional module must declare:

- module ID and version;
- required evidence profiles;
- required artifacts and fields;
- checks performed;
- not-applicable conditions;
- deterministic outputs;
- limitations;
- benchmark fixtures;
- expected false-positive and recall targets.

A module may add findings but may not override universal evidence, neutrality, severity, or validation safeguards.
