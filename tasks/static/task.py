from pyscript import Element, write, run_until_complete

task_started = False


def input_onClick():
    from datetime import datetime
    import asyncio

    task_start_time = datetime.now()

    async def foo():
        while True:
            await asyncio.sleep(0.1)
            Element("timerDisplay").write(f"{(datetime.now() - task_start_time).total_seconds()} s.")
            if Element("inputDisplay").value == Element("inputPractice").value:
                break

        Element("divSubmitScore").element.hidden = False
        Element("timerInput").element.type = "hidden"

        Element("timerInput").element.value = Element("timerDisplay").element.innerText

    global task_started
    if not task_started:
        task_started = True
        run_until_complete(foo())
