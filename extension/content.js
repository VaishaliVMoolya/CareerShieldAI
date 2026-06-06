function getJobData() {

    return {
        pageText: document.body.innerText
    };

}

chrome.runtime.onMessage.addListener(
(request, sender, sendResponse) => {

    if(request.action === "GET_JOB_DATA") {

        sendResponse(getJobData());

    }

});