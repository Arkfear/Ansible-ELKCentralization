#!/bin/bash

appid=$1
login=$2

curl http://10.1.10.91:9999/apid/plat/data/redis/_memberIdMap/put/${appid}/${login}
curl -X POST --data-urlencode "payload={\"channel\": \"#logstash_autorepair\", \"username\": \"webhookbot\", \"text\": \"logstash is now repair appid:${appid}, login:${login}\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/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