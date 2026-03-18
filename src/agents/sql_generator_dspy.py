import dspy

class Text2SQL(dspy.Module):
    def __init__(self):
        self.generate = dspy.Predict("question, schema -> sql")

    def forward(self, question, schema):
        return self.generate(question=question, schema=schema)


#optimize

from dspy.teleprompt import BootstrapFewShot

optimizer = BootstrapFewShot()

optimized_model = optimizer.compile(
    student = Text2SQL(),
    trainset = train_data
)