#!/bin/bash

# Loop through telegraf_0 to telegraf_5
for i in {0..5}
do
  echo "Starting telegraf_$i..."
  nohup sudo docker-compose run --rm --entrypoint /bin/sh telegraf_$i -c "mkdir -p /root/.cache/snowflake && touch /root/.cache/snowflake/ocsp_response_cache.json && chmod 644 /root/.cache/snowflake/ocsp_response_cache.json && telegraf --debug --config /etc/telegraf/telegraf.conf" &
done

echo "All telegraf instances have been started."

