# Autonomous AI Video Generation Agent
**A Zero-Touch, Programmatic Pipeline for 3D Educational Shorts**

This project is a fully automated, end-to-end agentic workflow designed to generate high-fidelity, 3D-style educational videos. Unlike static automation tools, this system uses a custom Python orchestration engine to manage every stage of production—from initial brainstorming to final video assembly—without manual intervention.

---

##  Key Features

* **Autonomous Ideation:** Queries Gemini 2.5 Flash to brainstorm unique, viral-ready educational topics at runtime.
* **Persona-Driven Scripting:** Forces the LLM into a "Technical Director" persona to generate clinical, anatomical 3D scene descriptions.
* **High-End 3D Visuals:** Interfaces with SDXL via custom routing, utilizing subsurface scattering and Unreal Engine 5 rendering prompts.
* **Dynamic Audio Synthesis:** Generates professional, documentary-style narration using Edge TTS.
* **Programmatic Assembly:** Automatically synchronizes multi-modal assets into a 9:16 vertical MP4 format using MoviePy.

---

##  Ingenuity & "Jugaad" (The Resourcefulness Factor)

To ensure high-quality output using free-tier resources, the pipeline includes several custom engineering workarounds:

* **The "Ken Burns" Resilience Layer:** Free-tier image-to-video APIs are often unstable. This pipeline includes a local fallback that automatically applies a dynamic 2.5D zoom/pan effect to static renders if an API timeout occurs, ensuring the video never crashes.
* **Security Bypass Logic:** Implements User-Agent spoofing to bypass Cloudflare bot protection (Error 530) on free inference routers.
* **Fail-Open Philosophy:** If the primary brainstorming AI is unavailable, the system defaults to a vetted internal library of high-engagement topics to guarantee a successful run.
