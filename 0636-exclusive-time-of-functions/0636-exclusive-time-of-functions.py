class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        logs_stack = []
        result = [0] * n

        for content in logs:
            log = Log(content)
            if log.is_start:
                logs_stack.append(log)
            else:
                top = logs_stack.pop()
                result[top.id] += log.time - top.time + 1
                if logs_stack:
                    result[logs_stack[-1].id] -= log.time - top.time + 1
        return result


class Log:
    def __init__(self, content):
        content = content.replace(" ", "")
        parts = content.split(":")
        self.id = int(parts[0])
        self.is_start = parts[1] == "start"
        self.time = int(parts[2])