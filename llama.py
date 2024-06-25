
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/s63iblap4zro/LLAMA2/workflows/workflow-e2a536"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="37333077c8614908af0e18dc4a1cbba9"
)
result = text_classfication_workflow.predict_by_bytes(b"I love you", input_type="text")
print(result.results[0].outputs[0].data)
