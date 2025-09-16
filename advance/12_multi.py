# try 코드 안에서 여러개의 예외가 발생한 경우...
import traceback

# 1. 생겨난 예외마다 각기 다른 처릴르 해주고 싶을 때
try:
    pass
except IOError:
    pass
except KeyboardInterrupt:
    pass
except ValueError:
    pass

# 2. 어떤 예외가 발생하던지 동일한 처리를 하고 싶을 때
try:
    pass
except Exception as e: # 예외의 최상위 부모이기 때문에 다른 자식 예외가 모두 다 들어옴. 그래서 디테일하게 무슨 예외인지는 모름.
    traceback.print_exc()