from openai import OpenAI

client = OpenAI(
    base_url="https://pygmalion.herdora.com/v1",
    api_key="hrd_06jZpLZePjG4r7qtB3jtFFa2qeKZmGrML4DPwKkU", # change this!!!
)

resp = client.chat.completions.create(
    model="Qwen/Qwen3-VL-235B-A22B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
                    },
                },
            ],
        }
    ],
)

print(resp.choices[0].message.content)
