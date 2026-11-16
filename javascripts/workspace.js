/* Progressive enhancements only. Every lesson and link works without this file. */
(() => {
  "use strict";
  let cleanup = () => {};

  function mountWorkspace() {
    cleanup();
    const controller = new AbortController();
    const options = { signal: controller.signal };
    const drawer = document.getElementById("__drawer");
    const rail = document.getElementById("workspace-topics");
    const toggle = document.querySelector("[data-workspace-menu]");
    const close = document.querySelector("[data-workspace-close]");
    const content = document.querySelector("[data-workspace-kind]");
    const outline = document.querySelector(".workspace-outline__details");
    const compact = window.matchMedia("(max-width: 1050px)");
    const mobile = window.matchMedia("(max-width: 900px)");

    function syncDrawer() {
      const open = Boolean(drawer && drawer.checked);
      if (toggle) {
        toggle.setAttribute("aria-expanded", String(open));
        toggle.setAttribute("aria-label", open ? "Close topic navigation" : "Open topic navigation");
      }
      if (rail) rail.inert = mobile.matches && !open;
    }
    function setDrawer(open, returnFocus = false) {
      if (!drawer) return;
      drawer.checked = open;
      drawer.dispatchEvent(new Event("change", { bubbles: true }));
      syncDrawer();
      if (returnFocus && toggle) toggle.focus();
      else if (open && rail) rail.querySelector("a[aria-current], a")?.focus();
    }
    if (toggle) toggle.addEventListener("click", () => setDrawer(!drawer?.checked), options);
    if (close) close.addEventListener("click", () => setDrawer(false, true), options);
    if (drawer) drawer.addEventListener("change", syncDrawer, options);
    if (rail) rail.addEventListener("click", event => {
      if (event.target.closest("a") && mobile.matches) setDrawer(false);
    }, options);
    document.addEventListener("keydown", event => {
      if (event.key === "Escape" && drawer?.checked) setDrawer(false, true);
      if (event.key === "Tab" && mobile.matches && drawer?.checked && rail) {
        const links = [...rail.querySelectorAll("a[href], button")].filter(node => node.offsetParent !== null);
        const first = links[0];
        const last = links[links.length - 1];
        if (event.shiftKey && (document.activeElement === first || !rail.contains(document.activeElement))) {
          event.preventDefault();
          last?.focus();
        } else if (!event.shiftKey && (document.activeElement === last || !rail.contains(document.activeElement))) {
          event.preventDefault();
          first?.focus();
        }
      }
    }, options);
    mobile.addEventListener("change", syncDrawer, options);
    syncDrawer();

    if (outline) {
      outline.open = !compact.matches;
      compact.addEventListener("change", () => { outline.open = !compact.matches; }, options);
      outline.addEventListener("click", event => {
        if (compact.matches && event.target.closest("a[href^='#']")) outline.open = false;
      }, options);
    }

    document.querySelector("[data-workspace-search]")?.addEventListener("click", () => {
      const search = document.getElementById("__search");
      if (search) {
        search.checked = true;
        search.dispatchEvent(new Event("change", { bubbles: true }));
      }
      document.querySelector("[data-md-component='search-query']")?.focus();
    }, options);

    if (content) {
      const topic = content.dataset.workspaceTopic;
      document.querySelectorAll("[data-workspace-topic-link]").forEach(link => {
        if (topic && link.dataset.workspaceTopicLink === topic) link.setAttribute("aria-current", "page");
        else link.removeAttribute("aria-current");
      });
      const title = document.querySelector("[data-workspace-header-topic]");
      if (title) title.textContent = content.dataset.workspaceTopicLabel || "Learning workspace";
    }
    const modes = [...document.querySelectorAll(".workspace-modes a")];
    const practice = modes.find(link => link.textContent.trim().toLowerCase() === "practice");
    if (practice) {
      const target = new URL(practice.href);
      if (target.pathname === window.location.pathname && target.hash) {
        const syncInlineMode = () => {
          const inPractice = window.location.hash === target.hash;
          modes.forEach(link => {
            const active = inPractice ? link === practice : link !== practice;
            if (active) link.setAttribute("aria-current", "page");
            else link.removeAttribute("aria-current");
          });
        };
        window.addEventListener("hashchange", syncInlineMode, options);
        syncInlineMode();
      }
    }
    cleanup = () => controller.abort();
  }

  if (typeof document$ !== "undefined") document$.subscribe(mountWorkspace);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mountWorkspace, { once: true });
  else mountWorkspace();
})();
