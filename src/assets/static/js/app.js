
const telegram = window.Telegram.WebApp;
telegram.ready();


async function authAndRedirect() {
    try {
        const response = await fetch("/webapp/auth/", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ initData: telegram.initData }),
        });

        const data = await response.json();

        console.log("data: ", data)
        console.log("data.redirect: ", data.redirect)
        if (data.redirect) {
            window.location.href = data.redirect;
        }

    } catch {
        console.log("SomeThing Wrong")
    }
}

document.addEventListener("DOMContentLoaded", () => {
    authAndRedirect();
});