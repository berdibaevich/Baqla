
const telegram = window.Telegram.WebApp;


async function authAndRedirect() {
    try {
        const response = await fetch("/webapp/auth/", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ initData: telegram.initData }),
        });

        const data = await response.json();

        console.log("data: ", data)

    } catch {
        console.log("SomeThing Wrong")
    }
}

document.addEventListener("DOMContentLoaded", () => {
    authAndRedirect();
});