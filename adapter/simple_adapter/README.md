Adapter Pattern

Main Components of pattern:
Client - contains existing business logic of application
Client Interface - Describes API that the client adheres to
Service - usually a third-party or legacy class that the client wants to use but cannot due to mismatched interface
Adapter - class that works to adapt the client interface to the service interface. It implements the client interface (aka Target interface) while wrapping the legacy class and translating the calls to the legacy API

Example use cases:
Program under development uses interface. There is a desire to leverage an old tool that adheres to an older interface. Rather than re-developing the old library you can add an adapter class to wrap the old code so that it adheres to the new interface
