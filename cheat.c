points
virual syncrhonious system cannot scale: succeptible to partion
Paas: You get access to flexible computing and storage infrastructure, coupled with a software platform (often tightly coupled)
GoogleAppEngine
Saas: You get access to software services, when you need them. Often
said to subsume SOA (Service Oriented Architectures).GoogleDocs
Iaas:AmazonEWS :Virtualization
Haas:LeastSecure


####################
Global Resource Manager (RM)
Scheduling
Per-server Node Manager (NM)
Daemon and server-specific functions
Per-application (job) Application Master (AM)
Container negotiation with RM and NMs
Detecting task failures of that job

NM heartbeats to RM
If server fails, RM lets all affected AMs know, and AMs take action
NM keeps track of each task running at its server
If task fails while in-progress, mark the task as idle and restart it
AM heartbeats to RM
On failure, RM restarts AM, which then syncs up with its running tasks

When you have 120 servers in the DC, the mean time to failure (MTTF) of the next machine is 1 month.

When you have 12,000 servers in the DC, the MTTF is about once every 7.2 hours!

DesirableProperties:CompletenEss,Accuracy,Speed,Scale
Gossip:Bandwidth_up:TimeToPropagte_down


####################

Paxos safety?
If some round has a majority (i.e., quorum) hearing proposed value v’ and accepting it (middle of Phase 2), then subsequently at each round either   : 1) the round chooses v’ as decision or 2) the round fails •   Proof   : –   Potential leader waits for majority of OKs in Phase 1 –   At least one will contain v’ (because two majorities or quorums always intersect) –   It will choose to send out v’ in Phase 2 •   Success requires a majority, and any two majority sets intersect Scale, On-demand access, data-intensive, new programming

WUE = Annual Water Usage / IT Equipment Energy (L/kWh) – low is good • PUE = Total facility Power / IT Equipment Power – low is good
(e.g., Google~1.11) 
CLOCKSKEW| M / (2 * MDR) |Given a maximum acceptable skew M between any pair of clocks, need to synchronize at least once every:time units
External Synchronization with D => Internal Synchronization with 2*D
----
|VectorTimeStamp:|Send:increment its ith element
|_Receive|Vi[i] = Vi[i] + 1
      Vi[j] = max(Vmessage[j], Vi[j]) for j ≠ i 
|_VT1 = VT2,  
|_   iff   (if and only if)
|_    VT1[i] = VT2[i], for all i = 1, … , N
|_VT1 ≤ VT2,  
|_   iff   VT1[i] ≤ VT2[i], for all i = 1, … , N
|_Two events are causally related iff
|_    VT1 < VT2,  i.e.,
|_   iff   VT1 ≤ VT2 & 
|_   there exists j such that 
|_  :1 ≤ j ≤ N & VT1[j] < VT2 [j]


#SNAPSHOT_ALGORITHM_CHANDY_LAMPORT
Whenever a process Pi receives a Marker message on an incoming channel Cji
 if (this is the first Marker Pi is seeing) 
Pi records its own state first
Marks the state of channel Cji as “empty”
for j=1 to N except i
Pi sends out a Marker message on outgoing channel Cij 
Starts recording the incoming messages on each of the incoming channels at Pi: Cji (for j=1 to N except i)
  else // already seen a Marker message
Mark the state of channel Cji as all the messages that have arrived on it since recording was turned on for Cji
______
AlltoAll:L=N/T
Gossip: N*logN/t(gossip) | N*log(N)/T 
Ideal:[log(PM(T))/log(Pm)]/T
SWIM:e/(e-1)

Cristian   :Error is at most (RTT-min2-min1)/2)|setTime:t + (RTT+min2-min1)/2
NTP   :o = (tr1 – tr2 + ts2 – ts1)/2|
Lamport    : max(localClock+messagTimestamp)
vector    : Vi[i] = Vi[i] + 1 && Vi[j] = max(Vmessage[j], Vi[j]) for j ≠ i
checkpointing   : can restart distributed application on failure
Garbage collection of objects   : objects at servers that don’t have any other objects (at any servers) with pointers to them
Deadlock detection   : Useful in database transaction systems
Termination of computation   : Useful in batch computing systems like Folding@Home, SETI@Home

FIFO:
NOMAX_increment_onlyWhileSending_receive_checkToDeliver!!!!
|_Send multicast at process Pj:
Set Pj[j] = Pj[j] + 1
Include new Pj[j] in multicast message as its sequence number
|_Receive multicast: 
If Pi receives a multicast from Pj with sequence number S in message
if (S == Pi[j] + 1) then 
   deliver message to application
   Set Pi[j] = Pi[j] + 1
else buffer this multicast until above condition is true

|||CAUSAL
Send multicast at process Pj:
Set Pj[j] = Pj[j] + 1
Include new entire vector Pj[1…N] in multicast message as its sequence number
Receive multicast: If Pi receives a multicast from Pj with vector                           M[1…N] (= Pj[1…N]) in message, buffer it until both:
This message is the next one Pi  is expecting from Pj, i.e., 
M[j] = Pi[j] + 1
All multicasts, anywhere in the group, which happened-before M have been received at Pi, i.e., 
For all k ≠ j: M[k] ≤ Pi[k]
i.e., Receiver satisfies causality 
When above two conditions satisfied, deliver M to application and set Pi[j]  = M[j]

SRM (Scalable Reliable Multicast)|Uses NAKs
But adds random delays, and uses exponential backoff to avoid NAK storms
RMTP (Reliable Multicast Transport Protocol)|Uses ACKs


#CHORD
At node n, send query for key k to largest successor/finger entry <= k
if none exist, send query to successor(n) 
Consistent Hashing => with K keys and N peers, each peer stores O(K/N) keys. (i.e., < c.K/N, for some constant c)
r=2log(N)|lookupCorrectNess

Name,Memory,Lookup,#messagesForLookup
Napster,O(1)/O(N)@server,O(1),O(1)
Chord,log(N),log(N),log(N)
Kelips,O(rootN),o(1),disseminationtime(ologn)
Safety:  For all non-faulty processes p: (p’s elected = (q: a particular non-faulty process with the best attribute value) or Null)
Liveness: For all election runs: (election run terminates) & for all non-faulty processes p: p’s elected is not Null
Election:
Ring:election|elected|worst:Best=3n-1:2n
Bully:election|ok|coordinator|worst:best=o(n)sq:N-2(onemessageTransmissionTime)
GoogleChubby:live & safe|quoram|voteOnce|masterLease|MutualExclusion_locking
__Bandwidth|#msg sent in each enter and exit.
__Clientdelay|delay incurred by a process at each enter and exit operation (when no other process is in, or waiting)
__SynchDelay|time between one process exiting the critical section and the next process entering it (when there is only one process waiting
****MutualExclusion:enter(),AccessResource(),exit()
  Safety|At most one process execute CS
  Liveness|Every request for a CS is granted eventually
  Ordering(desirable)|FIFO
CentralAlgorithm|safety+liveness|singlePointFailure|ordered@master
  Bandwidth:clientdelay:syncDelay=2 enter,1exit:2:2
RingBased|safe+live|noOrdering|
  BW:CD:SD=1,1:0-N:1-(N-1)
Ricart_Agarwala|NoToken|Multicast|LamportTime|casuality|ordered
RickartAgarwala
      ||enter() at process Pi
       set state to Wanted
       multicast “Request” <Ti, Pi> to all processes, where Ti = current Lamport timestamp at Pi
       wait until all processes send back “Reply”
       change state to Held and enter the CS
      ||On receipt of a Request <Tj, Pj> at Pi (i ≠ j):
      if (state = Held) or (state = Wanted & (Ti, i) < (Tj, j)) 
               add request to local queue (of waiting requests)
      else send “Reply” to Pj
      ||exit() at process Pi
       change state to Released and “Reply” to all queued requests.
  state"Wanted|Held|Released"|"Request|Reply"
  BW:CD:SD=2(N-1),(N-1):1:1
Maekawa|voting_set_k|non_emptyIntersection|votesAtMostOnce|NeedsVoteFromAll
DOES NOT GURANTEE LIVENESS|DEADLOCK|EACH WOULD VOTE FOR ITSELF
  state"Wanted|Held|Released"|"VotedFlag"|"Request|Reply|Release"
      When Pi receives a Request from Pj:
      if (state == Held OR voted = true)
         queue Request
      else
         send Reply to Pj and set voted = true

      When Pi receives a Release from Pj:
      if (queue empty)
         voted = false
      else
         dequeue head of queue, say Pk
         Send Reply only to Pk
         voted = true
  BW:CD:SD=2rootN,rootN:(N-1),1:2
FLP:SchedulesCommutative|Disjoint Schedules are commutative
s1={(p1,m1),(p2,m2),(p1,m1)}|s2={(p,m)}|p Not in s1
There always exists an initial config that is bivalent
starting from bivalent,there is always another bivalent config reachable
|Routing|NetworkLayer
|_DistanceVectorRouting(RIP)|Proactive|
|_Link-State(OSPF)
|_TCP:connectionless|decomposition|reliable:acks|mult/demult|congestion|FIFO_order
|_DNS|Recursive:may_fail_
|_Iterative_LocalNameServerMostResponsibilty>BETTER|longer but more control

RPC|CodeReuse|Dispatcher:inServer
|_LPC:exactlyOnce
|Concurrency|pessimistic|optimisitic
|_Pessimistic:locking(read|writeMode)|optimisticTwoPhaseLocking:serialEquivilance|GrowingPhase,ShrinkingPhase
|_Optimistic|firstCut,TimeStampOrder,MultiVersionControl
|_firstCutApproach:r/w@will-chk@commit-rollback:cascadingAborts
|_TimeStampOrder:read_if_lastW_by_lowerid,write_if_lastR_bylowerid
|_MultiVersionControl:multipleVers,readOnlyImmediatePrevious
EventualConsistency:Cassandra+Dynamo=lastWriteWins|
Riak=vectorClocks:sizeBased|TimeBasedPruning
#Replication|challenge|Transperancy+consistency
Why|Fault-tolerance|Load balancing|Replication => Higher Availability
What problem is this?Consensus!(It’s also called the “Atomic Commit problem”)
|1-f^k:K=#replica,f=probFailure:
|_Passive:Active=Master:treatAllSame
Transaction&Replication|NonReplicatedSystem:serialEquvilance
|_InReplicatedSys:serialEqui+OneCopySerializability:"""The effect of transactions performed by clients on replicated objects should be the same as if they had been performed one at a time on a single set of objects"""
TransactionCommit:OnePhase|TwoPhase|Coordinator:Prepare+Yes/No+Commit<LOG>
#KeyValueStore
|_Cassandra|ReplicationStatergy|Simple,Network
|_Simple:Random,ByteOrder<rangeQueries>|
|_NetworkTopology<DCWide+withinDC_RACK>:Snitches:Simple|RackInferring<x.<DC>.<rack>.<node>|PropertyFile|ECS:ECSRegion<DC>+AvailabilityZone<rack>
|_Writes|HintedHandOff:replicasDown:Timeout|memTable<Append>Cache|SSTABLE_disk
|_Reads|slow:BLOOM+INDEX+SSTABLE+MULTIPLEREPLICA+MULTIPLE_sstables_rows
|_PHI:toSetLongerTimeoutForSlowerServers|log(CDF or Probability(t_now – t_last))/log 10

|_Quoram:W:Coordinator:waitsFor_W_toRepsond||asynchronous<FAST>Write&Return
ANY: any server (may not be replica)
Fastest: coordinator may cache write and reply quickly to client
ALL: all replicas
Slowest, but ensures strong consistency
ONE: at least one replica|Faster than ALL, and ensures durability without failuresQUORUM: quorum across all replicas in all datacenters (DCs)|Global consistency, but still fast
LOCAL_QUORUM: quorum in coordinator’s DC|Faster: only waits for quorum in first DC client contacts|

EACH_QUORUM: quorum in every DC|Lets each DC do its own quorum: supports hierarchical replies
|_(W+N>N__W>N/2):
|_(W=1,R=1): very few writes and reads
|_(W=N, R=1): great for read-heavy workloads
|_(W=N/2+1, R=N/2+1): great for write-heavy workloads
|_(W=1, R=N): great for write-heavy workloads with mostly one client writing per key

MongoDB|consistent,shardKey:Primary|collectionOfChunks
|_ReadPrefernce=primary/secondary/nearest
|_Write="acknowledged":primaryAcksImmediately|Journalled+replicaAck
|_Oplog:InMemory:JournalledToHarddisklater
HBASE:
ColFamily:someNameToColumNfamily|colQualifier:actualColumninColumnFamily
#GraphProcessing
|_Storm:MasterNode<NIMBUS>|DistribeCode+Assigntask+MonitorFailures
|_Worker<SuperVisor>:onServer|listenToWorkAssignedToMachines
|_Zookeeper|Coordinator|savesState
|_Pregel:Master|MaintainServerList/RestartonFailure/WebUI
|_Worker|Processes its vertices
GraphPlotting:For consistentTime,Blocksize_should be larger(fetching twice)
sensorOS:staticVsDynamic|predictableRunTime+noMethodcanCauseotherFailMemory
DSM:Downside of Invalidate:FalseSharing:processShare
UpdateApproach:All can write at once,send only that part of the page updated|multicast
InvalidateBetter:UpdateApproach|lots of sharing|Writes are to small variables|Page sizes large
SelfStabilizing:Masking:TransparentToAPplicationLayer
hold Token if "if" true: on then execution pass token to next successor
process j is x[j]  {0, 1, 2, K-1}, where K > N
p0   if x[0] = x[N-1] then x[0] := x[0] + 1 
pj  j > 0    if x[j] ≠ x[j -1] then x[j] := x[j-1] 
One-copy update semantics: when file is replicated, its contents, as visible to clients, are no different from when the file has exactly 1 replica







