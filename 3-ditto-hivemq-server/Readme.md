## Eclipse Ditto Server
Contains
1. kafka-IOT broker
2. ditto-hivemq cluster
3. mongo-db temporary/backup database 

---

## Start the container cluster

```bash
docker-compose up --build -d
```
## URLs
1. producer endpoints => http://IP:8000/topic-1,http://IP:8000/topic-2,http://IP:8000/topic-3
2. kafka-IOT-broker UI => http://IP:19000
3. hivemq UI => http://IP:8181
4. diito UI => http://IP:8080
5. mogodb backup db => http://IP:27017 

## Basic curl commands to configure ditto
1.create a policy
```

	curl -X PUT 'http://localhost:8080/api/2/policies/ditto.default:policy' -u 'ditto:ditto' -H 'Content-Type: application/json' -d '{
	"entries": {
    	"owner": {
        	"subjects": {
            	"nginx:ditto": {
                	"type": "nginx basic auth user"
            	}
        	},
        	"resources": {
            	"thing:/": {
                	"grant": [
                    	"READ","WRITE"
                	],
                	"revoke": []
            	},
            	"policy:/": {
                	"grant": [
                    	"READ","WRITE"
                	],
                	"revoke": []
            	},
            	"message:/": {
                	"grant": [
                    	"READ","WRITE"
                	],
                	"revoke": []
            	}
        	}
    	},
    	"connection": {
        	"subjects": {
            	"connection:hivemq-mqtt": {
                	"type": "Connection to HiveMQ MQTT broker"
            	}
        	},
        	"resources": {
            	"thing:/": {
                	"grant": [
                    	"READ","WRITE"
                	],
                	"revoke": []
            	},
            	"message:/": {
                	"grant": [
                    	"READ","WRITE"
                	],
                	"revoke": []
            	}
        	}
    	}
	}
}'

```

2. create a thing

```

	curl -X PUT 'http://localhost:8080/api/2/things/traffic-intersection.test:Sensor_Road1' -u 'ditto:ditto' -H 'Content-Type: application/json' -d '{
	    "policyId": "ditto.default:policy",
	    "attributes": {
		"name": "Sensor_Road1",
		"type": "IP Camera",
		"location": "Peradeniya"
	    },
	    "features": {
		"index": {
		    "properties": {
		        "value": 0
		    }
		},
		"timestamp": {
		    "properties": {
		        "value": "00:00:00"
		    }
		},
		"date": {
		    "properties": {
		        "value": "00"
		    }
		},
		"day_of_week": {
		    "properties": {
		        "value": "Monday"
		    }
		},
		"car_count": {
		    "properties": {
		        "value": 0
		    }
		},
		"bike_count": {
		    "properties": {
		        "value": 0
		    }
		},
		"bus_count": {
		    "properties": {
		        "value": 0
		    }
		},
		"truck_count": {
		    "properties": {
		        "value": 0
		    }
		},
		"total": {
		    "properties": {
		        "value": 0
		    }
		},
		"traffic_situation": {
		    "properties": {
		        "value": "unknown"
		    }
		}
	    }
	}'
	
```
3. connect to hivemq
```
	curl -X POST 'http://localhost:8080/api/2/connections' -u 'devops:foobar' -H 'Content-Type: application/json' -d '{
	    "name": "HiveMQ",
	    "connectionType": "mqtt",
	    "connectionStatus": "open",
	    "failoverEnabled": true,
	    "uri": "tcp://hivemq:1883",
	    "sources": [{
		"addresses": ["devices/#"],
		"authorizationContext": ["connection:hivemq-mqtt"],
		"qos": 1,
		"enforcement": {
		    "input": "{{ source:address }}",
		    "filters": [
		        "devices/{{ thing:id }}"
		    ]
		}
	    }],
	    "targets": [{
		"address": "devices/{{ thing:id }}/downlink",
		"topics": [
		    "_/_/things/twin/events",
		    "_/_/things/live/messages"
		],
		"authorizationContext": ["connection:hivemq-mqtt"],
		"qos": 1
	    }]
	}'


```

4. payload mapping (in ditto ui: connections)

```
	function mapToDittoProtocolMsg(headers, textPayload, bytePayload, contentType) {
	    const jsonString = String.fromCharCode.apply(null, new Uint8Array(bytePayload));
	    const jsonData = JSON.parse(jsonString); 
	    const thingId = jsonData.thingId.split(':'); 
	    const value = { 
		index: { 
		    properties: { 
		        value: jsonData.index 
		    } 
		},
		timestamp: { 
		    properties: { 
		        value: jsonData.timestamp 
		    } 
		},
		date: { 
		    properties: { 
		        value: jsonData.date 
		    } 
		},
		day_of_week: { 
		    properties: { 
		        value: jsonData.day_of_week 
		    } 
		},
		car_count: { 
		    properties: { 
		        value: jsonData.car_count 
		    } 
		},
		bike_count: { 
		    properties: { 
		        value: jsonData.bike_count 
		    } 
		},
		bus_count: { 
		    properties: { 
		        value: jsonData.bus_count 
		    } 
		},
		truck_count: { 
		    properties: { 
		        value: jsonData.truck_count 
		    } 
		},
		total: { 
		    properties: { 
		        value: jsonData.total 
		    } 
		},
		traffic_situation: { 
		    properties: { 
		        value: jsonData.traffic_situation 
		    } 
		}   
	    };    
	    return Ditto.buildDittoProtocolMsg(
		thingId[0], // your namespace 
		thingId[1], 
		'things', // we deal with a thing
		'twin', // we want to update the twin
		'commands', // create a command to update the twin
		'modify', // modify the twin
		'/features', // modify all features at once
		headers, 
		value
	    );
	}


```

## Managing the container cluster

Check the logs after starting up:
```bash
docker-compose logs -f
```

Check the resource consumption in order to find out if you e.g. require more memory:
```bash
docker stats
```

## Stop Eclipse Ditto

```bash
docker-compose down
```
