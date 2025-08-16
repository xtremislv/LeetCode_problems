import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    a = [x[0] for x in student_data]
    b = [x[1] for x in student_data]
    c = {'student_id': a , 'age': b}
    df = pd.DataFrame(c)
    return df