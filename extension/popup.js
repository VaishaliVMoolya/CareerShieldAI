document
.getElementById("analyzeBtn")
.addEventListener("click", async () => {

    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    chrome.tabs.sendMessage(
        tab.id,
        {
            action: "GET_JOB_DATA"
        },
        (response) => {

            document.getElementById("result").innerText =
                response.pageText.substring(0,1000);

        }
    );

});