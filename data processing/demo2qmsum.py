"""
This script was used to convert the original Aveni transcript and qeuries into the same format as QMSum.
The final manual annotated data is provided in Data/Aveni/all
"""

import json

with open("/Users/terra/Desktop/diss/demoRobbieTranscript.json", "r") as demo:
     demo_transcript = json.load(demo)

with open("/Users/terra/Desktop/diss/demo_call_alessandra.json", "r") as demo:
     demo_data = json.load(demo)

demo_new_format = {
    "topic_list": [], #list of dictionaries {topic, list of relevant text spans}
    "general_query_list": [], #list of dictionaries {query (general summary of a topic), answer}
    "specific_query_list": [], #list of dictionaries {query, answer, list of relevant text spans}
    "meeting_transcripts": []
}

topic_list = []
specific_topic_list = []
specific_query_list = []
for dict in demo_data:
    for key, value in dict.items():
        if key == "title_topic" and value not in topic_list:
             topic_list.append(value)
             # for general_query_list use title_topic from re-summarize task
             demo_new_format["general_query_list"].append({
            "query": "Summarize %s" % value,
            "answer": "..."
        })
        if key == "partitions":
             for part_dict in value:
                  for k, val in part_dict.items():
                       if k == "partition_results":
                            for k_res, val_res in val.items():        
                                # for topic_list use topic from topic scan task
                                 if k_res == "topic" and val_res not in specific_topic_list:
                                    specific_topic_list.append(val_res)
                                    demo_new_format["topic_list"].append({
                                    "topic": val_res,
                                    "relevant_text_span": []
                                    } )   
                                 # for specific_query_list use question_topic from summary questions task                                   
                                 if k_res == "question_topic" and val_res not in specific_query_list: 
                                      specific_query_list.append(val_res)
                                      demo_new_format["specific_query_list"].append({
                                        "query": val_res,
                                        "answer": "...",
                                        "relevant_text_span": []
                                    })

line = 0
for i in demo_transcript["monologues"]:
    line += 1
    if i["spk"] == 0:
         speaker = "Adviser"
    else: 
         speaker = "Client"
    demo_new_format["meeting_transcripts"].append({
            "speaker": speaker,
            "content": i["text"],
            "line": line - 1     
        })
    


with open('demo_new_format.json', 'w') as f:
    json.dump(demo_new_format, f, indent= 4)


# demoRobbieTranscript.json structure
"""
{
  "monologues": [
    {
      "spk": 1,
      "ts": 2928.01,
      "dur": 0.76,
      "text": "Excellent. Thanks very much."      # repeat x each utterance
    }
  ],
  "speakers": [
    {
      "type": "internal",
      "displayName": "Alan Adviser"
    },
    {
      "type": "external",
      "displayName": "Mr Smith"
    }
  ]
}

"""
# QMSum structure

"""
{
    "topic_list": [
        {
            "topic": "...",
            "relevant_text_span": [
                [
                    "19",
                    "89"
                ]
            ]
        }           # repeat x each topic
    ],
    "general_query_list": [
        {
            "query": "Summarize the whole meeting",
            "answer": "..."
        }
    ],
    "specific_query_list": [
        {
            "query": "...",
            "answer": "...",
            "relevant_text_span": [
                [
                    "19",
                    "89"
                ]             # can have multiple text spans
            ]
        },                    # repeat x each query
        
    ],
    "meeting_transcripts": [
        {
            "speaker": "...",
            "content": "..."       # repeat x each utterance
        },
     ]
}
"""