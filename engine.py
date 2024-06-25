
from wenxin_engine import wenxin_engine
from Llama3_engine import Llama3_engine
from config import ITER
USE_CACHE= False




def connect2llm(engine,accumulate,insight, info_blocks,personality_requirements
                ,testing_methods,capacity):
    prompt = "请根据该需求生成测试用例。"+capacity +insight+ """你的回答应该细致、具体，并针对每个可能出现的边界情况编写尽可能多并且全面的测试用例。"""+ personality_requirements+f'要求测试用例严格包含以下信息作为每列的标题：{info_blocks}。如果没有信息，可以在那个位置放"无"但不能不放信息。'+ testing_methods + '测试用例输出的格式使用表格格式。'
    
    if engine == '百度/文心一言/ERNIE-Speed':
        return wenxin_engine(prompt,iter=ITER,accumulate=accumulate)
    elif engine == 'Llama3_Instruct':
        return Llama3_engine(prompt)
