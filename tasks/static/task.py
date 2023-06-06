from pyscript import Element, write, run_until_complete

task_start_time = None
task_complete = False


def input_onClick():
    from datetime import datetime
    import asyncio

    task_start_time = datetime.now()

    async def foo():
        while True:
            await asyncio.sleep(0.1)
            Element("timer").write(f"{(datetime.now() - task_start_time).total_seconds()} s.")
            if Element("inputDisplay").value == Element("inputPractice").value:
                break

        Element("divSubmitScore").element.hidden = False

    run_until_complete(foo())

