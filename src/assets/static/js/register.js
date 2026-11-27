(() => {
  const form = document.getElementById("student-reg");
  const steps = [...form.querySelectorAll(".step")];
  const bar = document.getElementById("progress-bar");
  const label = document.getElementById("progress-label");
  const ghInput = document.getElementById("id_github_username");
  const ghStatus = document.getElementById("gh-status");
  const ghLoader = document.getElementById("gh-loader");
  const ghNext = document.getElementById("gh-next");

  let cur = 0;

  function show(i) {
    cur = i;
    steps.forEach((s, k) => (s.hidden = k !== i));
    const pct = Math.round(((i + 1) / steps.length) * 100);
    bar.style.width = pct + "%";
    label.textContent = pct + "%";
  }

  function validateStep() {
    for (const f of steps[cur].querySelectorAll("input, select")) {
      if (!f.checkValidity()) { f.reportValidity(); return false; }
    }
    return true;
  }

  async function checkGithub() {
    ghLoader.hidden = false;
    ghNext.disabled = true;
    ghStatus.textContent = "Tekserilmekte...";
    ghStatus.className = "";

    let exists = false;
    try {
      const r = await fetch(`/webapp/check-github/?username=${encodeURIComponent(ghInput.value.trim())}`);
      exists = (await r.json()).exists;
    } catch (e) {}

    ghLoader.hidden = true;
    ghNext.disabled = false;
    ghStatus.textContent = exists ? "OK" : "Tabilmadi";
    ghStatus.className = exists ? "ok" : "bad";
    return exists;
  }

  form.querySelectorAll(".next").forEach((btn) =>
    btn.addEventListener("click", async () => {
      if (!validateStep()) return;
      if (btn === ghNext && !(await checkGithub())) return;
      show(cur + 1);
    })
  );

  form.querySelectorAll(".back").forEach((btn) =>
    btn.addEventListener("click", () => show(cur - 1))
  );

  show(0);
})();