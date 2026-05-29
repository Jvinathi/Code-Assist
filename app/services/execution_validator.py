import asyncio
from playwright.async_api import async_playwright


async def validate_app(app_path):

    results = {
        "success": True,
        "errors": [],
        "console_errors": []
    }

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        page = await browser.new_page()

        # ---------------------------------
        # CAPTURE CONSOLE ERRORS
        # ---------------------------------

        page.on(
            "console",
            lambda msg: (
                results["console_errors"].append(
                    msg.text
                )
                if msg.type == "error"
                else None
            )
        )

        try:

            await page.goto(
                f"file:///{app_path}"
            )

            await page.wait_for_timeout(3000)

            buttons = await page.query_selector_all(
                "button"
            )

            print(f"\nFOUND {len(buttons)} BUTTONS")

            for button in buttons[:5]:

                try:

                    await button.click()

                    print("BUTTON CLICKED")

                    await page.wait_for_timeout(1000)

                except Exception as e:

                    results["errors"].append(
                        str(e)
                    )

            # ---------------------------------
            # CHECK CONSOLE ERRORS
            # ---------------------------------

            if results["console_errors"]:

                results["success"] = False

            print("\nCONSOLE ERRORS:")

            for error in results["console_errors"]:

                print(error)

            await page.wait_for_timeout(15000)

        except Exception as e:

            results["success"] = False

            results["errors"].append(str(e))

        await browser.close()

    return results


def run_validation(app_path):

    return asyncio.run(
        validate_app(app_path)
    )