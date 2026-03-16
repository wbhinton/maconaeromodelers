# Concept Map

Domain concepts, terminology, and relationships for Macon Aero Modelers website.

## Core Concepts

### Entities

| Concept | Type | Description |
|---------|------|-------------|
| Macon Aero Modelers | entity | Western North Carolina radio-controlled model aircraft club, AMA Charter #3114, Gold Leader Club |
| Academy of Model Aeronautics (AMA) | entity | National organization providing liability insurance and governance for model aviation clubs |
| Membership | entity | Club membership requires paid annual dues, AMA membership, and sponsorship by current member |
| Board of Directors (BOD) | entity | Governing body: President, Vice-President, Secretary, Treasurer, Safety Officer, Field Maintenance Officer, PR Officer, 2 Directors at Large |
| Safety Officer | entity | Elected official enforcing AMA and club safety rules, assessing fines for violations |
| Flying Field | entity | Physical location at 516 Tessentee Road, Otto, NC with turf runway |
| Treasurer | entity | Elected officer managing club finances, membership records, dues collection |
| Visitor | entity | Non-member pilot permitted to fly up to 3 times per calendar year without dues |
| Dues | entity | Annual membership fee set by BOD; due Jan 1, 90-day grace period |

### Concepts

| Concept | Description |
|---------|-------------|
| FAA Compliance | Federal aviation regulations members should follow; recommended but not mandatory |

## Terminology

| Term | Definition |
|------|------------|
| AMA Gold Leader Club | Elite status designation for clubs demonstrating excellence in safety and operations |
| Charter Club #3114 | Official AMA club registration number |
| Flight Safety Issues | Complaints or incidents relating to safe flying operations |
| Quorum | Minimum number of members required to conduct official club business (5 BOD members) |
| Fiscal Year | Club financial cycle: January 1 through December 31 |
| Honorary Member | Title granted by BOD; exempt from dues, no voting rights |
| Sponsored Member | Member whose dues are suspended by BOD in recognition of club contributions |
| Director at Large | Elected board position to fill gaps as needed |
| Pro Tem | Temporary officer designation when substitution is unclear |

## Relationships

- **Membership → AMA**: All members must maintain current AMA membership for insurance coverage
- **Membership → Dues**: Annual dues payment required for active membership status
- **Safety Officer → Board of Directors**: Safety Officer notifies BOD of repeated violations
- **Treasurer → Membership**: Processes applications, verifies AMA status
- **Visitor → AMA**: Visitors must provide AMA proof of insurance before flying
- **President → Board of Directors**: Chairs BOD meetings
- **Flying Field → Macon Aero Modelers**: Club maintains field at Tessentee Road
- **New Member → Sponsor**: New members require sponsorship by existing club member

## Contexts

### Club Governance
- **Scope**: Constitution & Bylaws
- **Concepts**: Officer structure, Voting procedures, Amendments, Meeting quorum
- **Boundaries**: All policy decisions require membership vote; BOD handles day-to-day operations

### Financial Operations
- **Scope**: Treasury
- **Concepts**: Dues collection, Payment processing, Membership records, Non-refundable policy
- **Boundaries**: Treasurer manages all money; requires President approval for purchases over $100

### Safety Operations
- **Scope**: Flying Field
- **Concepts**: AMA compliance, FAA guidance, Visitor limits, Safety enforcement
- **Boundaries**: Safety Officer has field authority; can assess fines; must report to BOD

## Cross-Cutting Concerns

### Insurance & Liability
- AMA membership mandatory - no insurance means no flying
- Affects: Membership eligibility, Visitor policy, Safety enforcement

### Documentation
- Written constitutions with revision history
- Minutes maintained by Secretary; Treasurer maintains financial records
- Affects: Officer transitions (30-day handoff), Constitutional amendments (30-day notice)

### Digital Infrastructure
- Club website at maconaeromodelers.com
- Electronic application submission preferred
- Affects: PR Officer role, Membership communication, Document distribution

## Patterns

- **Membership Application Workflow**: 5-step process (application → Treasurer → BOD review → welcome email)
- **Annual Dues Cycle**: Due Jan 1; 90-day grace; reminder March 31; resign after 90 days if unpaid
- **Officer Election**: Nominating Committee in November; election at December meeting; 1-year term
- **Visitor Flying Policy**: 3 flights per calendar year without dues; must show AMA card
- **Disciplinary Escalation**: Safety Officer → BOD → 2/3 member vote for expulsion
