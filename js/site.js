const toggle = document.querySelector(".menu-toggle");
const panel = document.querySelector("#mobile-nav");
const openIcon = document.querySelector("[data-open]");
const closeIcon = document.querySelector("[data-close]");

if (toggle && panel) {
  toggle.addEventListener("click", () => {
    const open = panel.hasAttribute("hidden") === false;
    if (open) {
      panel.setAttribute("hidden", "");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open menu");
      openIcon.hidden = false;
      closeIcon.hidden = true;
    } else {
      panel.removeAttribute("hidden");
      toggle.setAttribute("aria-expanded", "true");
      toggle.setAttribute("aria-label", "Close menu");
      openIcon.hidden = true;
      closeIcon.hidden = false;
    }
  });
}

const form = document.querySelector("#contact-form");
if (form) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = document.querySelector("#name")?.value ?? "";
    const email = document.querySelector("#email")?.value ?? "";
    const org = document.querySelector("#org")?.value ?? "";
    const message = document.querySelector("#message")?.value ?? "";
    const body = ["Name: " + name, "Email: " + email, org ? "Organization: " + org : null, "", message]
      .filter(Boolean)
      .join("\n");
    window.location.href =
      "mailto:hello@aurelianware.com?subject=" +
      encodeURIComponent("Aurelianware inquiry") +
      "&body=" +
      encodeURIComponent(body);
  });
}
