Basic Overview of the Software Environment 




```
+----------------------------------------------------+
|     Docker Host(Local Machie)                      |
+----------+-----------------------------------------+
                |                            |
                |                            |
 Real           |                            | Simulated
 Twin           |                            | Twin
 (Soft-Sensors) |                            |
                v                            v 
+----------------------+    +--------------------------+
|   Kubernetes Cluster |    |    Simulation            |
|                      |    |(another docker container)|
|    Sensor_1          |    |                          |
|    +--------------+  |    |     1. Dashboard         |
|    |  Pod         |  |    |       i.Visulizations    |
|    |  +----------+|  |    |       ii.ML Analysis     |
|    |  | Container||  |    |     2. 3D simulation     |
|    |  +----------+|  |    |                          |
|    +--------------+  |    +--------------------------+
|                      |
|    Sensor_2          |
|    +--------------+  |
|    |  Pod         |  |
|    |  +----------+|  |
|    |  | Container||  |
|    |  +----------+|  |
|    +--------------+  |
|            .         |
|            .         |
|            .         |
|                      |
|    Sensor_6          |
|    +--------------+  |
|    |  Pod         |  |
|    |  +----------+|  |
|    |  | Container||  |
|    |  +----------+|  |
|    +--------------+  |
+----------------------+
           |
           |
           v
+----------------------+
|  Kubernetes Services |
|                      |
|    +--------------+  |
|    |  Service     |  |
|    |              |  |
|    +--------------+  |
|    +--------------+  |
|    |  Service     |  |
|    |(load balancer)  |
|    +--------------+  |
|    +--------------+  |
|    |  Service     |  |
|    |              |  |
|    +--------------+  |
+----------------------+
```


Initially Considering Only a "T jucntion"'s traffic flow intersection 
* vehicle flow,
* traffic congestion,
* signal timings(dynamic cycle calculation)
* later/optional(take pedestrian behaviours into consideration)

 Assuming 6 sensor's gather data; 2 per each road and catergorizing into all possible 6 phases (Therefore 6 pods) 
