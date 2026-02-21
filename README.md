# Awesome Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of AI agent platforms, frameworks, protocols, tools, and resources.

AI agents are autonomous software entities that perceive their environment, make decisions, and take actions to achieve goals. This list covers the rapidly evolving ecosystem of agent infrastructure -- from multi-agent frameworks and social platforms to blockchain reward systems and inter-agent communication protocols.

## Contents

- [Platforms](#platforms)
- [Frameworks](#frameworks)
- [Agent-to-Agent Protocols](#agent-to-agent-protocols)
- [Video and Media](#video-and-media)
- [Social and Community](#social-and-community)
- [Blockchain and Rewards](#blockchain-and-rewards)
- [Monitoring and Observability](#monitoring-and-observability)
- [SDKs and Libraries](#sdks-and-libraries)
- [Standards and Specifications](#standards-and-specifications)
- [Research and Papers](#research-and-papers)
- [Contributing](#contributing)

---

## Platforms

*Hosted platforms and services for building, deploying, and running AI agents.*

- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - An experimental open-source attempt to make GPT-4 fully autonomous.
- [AgentGPT](https://github.com/reworkd/AgentGPT) - Assemble, configure, and deploy autonomous AI agents in your browser.
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - An AI-powered task management system that uses OpenAI and vector databases to create and execute tasks.
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - A dev-first open-source autonomous AI agent framework with tools, logs, and agent provisioning.
- [MetaGPT](https://github.com/geekan/MetaGPT) - Multi-agent framework that assigns different roles to GPTs to form a collaborative software entity.
- [OpenDevin](https://github.com/OpenDevin/OpenDevin) - An open-source platform for autonomous software engineering agents.
- [Devin](https://devin.ai/) - The first AI software engineer, capable of planning, coding, and deploying autonomously.
- [Replit Agent](https://replit.com/agent) - An AI agent that builds entire applications from natural language descriptions inside the Replit IDE.
- [Cursor](https://cursor.sh/) - An AI-first code editor with built-in agent capabilities for multi-file editing and codebase reasoning.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic's agentic coding tool that lives in your terminal and understands your entire codebase.
- [Copilot Workspace](https://githubnext.com/projects/copilot-workspace) - GitHub's task-centric AI environment for planning, implementing, and testing code changes.
- [BoTTube](https://bottube.ai) - A video-first social platform where AI agents create, share, and interact with video content autonomously.
- [Moltbook](https://moltbook.com) - A Reddit-style social platform with submolt communities where AI agents and humans coexist.
- [OpenClaw](https://openclaw.org) - An open agent directory and discovery platform for registering and finding AI agents across the web.
- [E2B](https://github.com/e2b-dev/e2b) - Open-source cloud runtime for AI agents providing sandboxed environments for code execution.
- [Wordware](https://www.wordware.ai/) - A natural language programming platform for building AI agents without traditional code.
- [Relevance AI](https://relevanceai.com/) - A platform for building and deploying AI agents and multi-step workflows with no code.
- [Flowise](https://github.com/FlowiseAI/Flowise) - Drag-and-drop UI to build customized LLM orchestration flows and AI agents.
- [Dify](https://github.com/langgenius/dify) - An open-source LLM app development platform with agent workflow orchestration.
- [Letta](https://github.com/letta-ai/letta) - A framework for creating stateful LLM agents with long-term memory (formerly MemGPT).

## Frameworks

*Libraries and frameworks for building agent systems programmatically.*

- [LangChain](https://github.com/langchain-ai/langchain) - A framework for developing applications powered by language models with chains, agents, and retrieval.
- [LlamaIndex](https://github.com/run-llama/llama_index) - A data framework for connecting custom data sources to large language models.
- [CrewAI](https://github.com/crewAIInc/crewAI) - A framework for orchestrating role-playing autonomous AI agents that work together as a crew.
- [Autogen](https://github.com/microsoft/autogen) - Microsoft's framework for building multi-agent conversational AI systems.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's SDK for integrating LLMs into apps with planners, plugins, and agent patterns.
- [Phidata](https://github.com/phidatahq/phidata) - A toolkit for building AI assistants with memory, knowledge, and tool use.
- [Haystack](https://github.com/deepset-ai/haystack) - An end-to-end NLP framework for building production-ready LLM applications and agents.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Agent framework from the creators of Pydantic, designed for production-grade type-safe agent development.
- [Swarm](https://github.com/openai/swarm) - OpenAI's experimental lightweight multi-agent orchestration framework.
- [Smolagents](https://github.com/huggingface/smolagents) - Hugging Face's minimalist library for building powerful agents in a few lines of code.
- [LangGraph](https://github.com/langchain-ai/langgraph) - A library for building stateful, multi-actor applications with LLMs using graph-based workflows.
- [DSPy](https://github.com/stanfordnlp/dspy) - Stanford's framework for programming with foundation models through declarative modules rather than prompting.
- [Rivet](https://github.com/Ironclad/rivet) - A visual programming environment for building complex AI agent workflows with a node-based editor.
- [Composio](https://github.com/ComposioHQ/composio) - A platform providing 250+ tool integrations for AI agents across popular frameworks.
- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - A toolkit from Coinbase for building AI agents with onchain capabilities and wallet management.
- [Vercel AI SDK](https://github.com/vercel/ai) - A TypeScript toolkit for building AI-powered applications with streaming, tool calling, and agent support.
- [Instructor](https://github.com/instructor-ai/instructor) - A library for structured data extraction from LLMs using Pydantic models.
- [Camel](https://github.com/camel-ai/camel) - A communicative agents framework for exploring multi-agent cooperation and competition.
- [Agency Swarm](https://github.com/VRSEN/agency-swarm) - A framework for creating collaborative swarms of AI agents based on the agency model.
- [TaskWeaver](https://github.com/microsoft/TaskWeaver) - Microsoft's code-first agent framework for converting natural language requests into executable code.

## Agent-to-Agent Protocols

*Protocols and standards for agents to discover, communicate with, and delegate tasks to other agents.*

- [Google A2A](https://github.com/google/A2A) - Google's open Agent-to-Agent protocol enabling interoperable communication between AI agents.
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) - Anthropic's open protocol for connecting AI models to external data sources and tools.
- [OpenClaw Beacon](https://github.com/Scottcjn/beacon-skill) - A decentralized agent discovery and liveness protocol where agents broadcast capabilities via heartbeat pings.
- [Grazer](https://github.com/Scottcjn/grazer-skill) - A multi-platform social agent protocol enabling bots to post, reply, and interact across 9+ platforms from one SDK.
- [Agent Protocol](https://github.com/AI-Engineer-Foundation/agent-protocol) - A common interface specification for communicating with AI agents regardless of their underlying implementation.
- [Agora Protocol](https://github.com/agoraprotocol/agora) - An open protocol for agent-to-agent marketplace interactions and task negotiation.
- [LMOS](https://github.com/eclipse-lmos/lmos) - Eclipse's Language Model Operating System for managing multi-agent deployments at enterprise scale.

## Video and Media

*Platforms and tools for AI-generated video, image, and multimedia content.*

- [BoTTube](https://bottube.ai) - An AI-native video platform where agents generate, upload, and curate video content with social engagement.
- [Runway](https://runwayml.com/) - An applied AI research company building creative tools including Gen-2 video generation.
- [Pika](https://pika.art/) - An AI video generation platform that creates and edits videos from text and images.
- [InVideo AI](https://invideo.io/ai/) - An AI-powered video creation tool that turns text prompts into publish-ready videos.
- [LTX Studio](https://ltx.studio/) - An AI filmmaking platform for creating full video productions with characters, scenes, and effects.
- [HeyGen](https://www.heygen.com/) - An AI video generation platform specializing in talking avatar videos and video translation.
- [Synthesia](https://www.synthesia.io/) - An enterprise AI video platform for creating professional videos with AI avatars and voices.
- [Luma Dream Machine](https://lumalabs.ai/dream-machine) - An AI model that generates realistic and fantastical videos from text and images.
- [Kling AI](https://klingai.com/) - A video generation model from Kuaishou capable of high-fidelity 1080p video synthesis.
- [Sora](https://openai.com/sora) - OpenAI's text-to-video model for generating realistic and imaginative video scenes.
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - A powerful modular node-based UI for Stable Diffusion and other generative AI pipelines.

## Social and Community

*Social platforms, directories, and community hubs for AI agents.*

- [Moltbook](https://moltbook.com) - A Reddit-style social platform with community-driven submolts where AI agents participate alongside humans.
- [ClawCities](https://clawcities.com) - A virtual world and agent directory where AI agents claim territories and interact in themed zones.
- [4Claw](https://4claw.com) - An anonymous imageboard-style platform for AI agents to post freely across topic boards.
- [Clawsta](https://clawsta.com) - An Instagram-style visual social network for AI agents to share images and stories.
- [AgentChan](https://agentchan.com) - A community hub for discovering and following AI agents across multiple platforms.
- [SwarmHub](https://swarmhub.ai) - A coordination layer for multi-agent swarms enabling discovery, pairing, and task delegation.
- [Agent Directory](https://agentdirectory.ai) - A searchable registry of AI agents with profiles, capabilities, and contact information.
- [Character.AI](https://character.ai/) - A platform for creating and chatting with AI characters that have distinct personalities.
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) - A locally hosted UI for interacting with AI characters through various LLM backends.
- [Hugging Face Spaces](https://huggingface.co/spaces) - A platform for hosting and sharing machine learning demos and AI applications.

## Blockchain and Rewards

*Blockchain networks, tokens, and reward systems for AI agents.*

- [RustChain](https://github.com/Scottcjn/Rustchain) - A Proof-of-Antiquity blockchain that rewards vintage and exotic hardware miners with RTC tokens.
- [wRTC Token (Solana)](https://solscan.io/token/12TAdKXxcGf6oCv4rqDz2NkgxjyHq6HQKoxKZGf5i4X) - The wrapped RTC token bridged to Solana with a Raydium liquidity pool.
- [wRTC Token (Base)](https://basescan.org/token/0x5683C10596AaA09AD7F4eF13CAB94b9b74A669c6) - The wrapped RTC token on Base L2 with an Aerodrome liquidity pool.
- [x402 Payment Protocol](https://github.com/coinbase/x402) - Coinbase's HTTP 402-based micropayment protocol enabling agents to pay for API access natively.
- [Fetch.ai](https://github.com/fetchai/fetchd) - A decentralized machine learning platform with autonomous economic agents on a dedicated blockchain.
- [Autonolas](https://github.com/valory-xyz/open-autonomy) - A platform for creating and deploying autonomous agent services on-chain.
- [Virtuals Protocol](https://www.virtuals.io/) - A protocol for co-owning and tokenizing AI agents on-chain with revenue sharing.
- [ai16z ELIZA](https://github.com/ai16z/eliza) - A multi-agent simulation framework enabling AI agents to interact on social media and manage crypto wallets.
- [Morpheus](https://github.com/MorpheusAIs/Morpheus) - A decentralized network of personal AI agents connected to smart contracts and crypto wallets.
- [SingularityNET](https://github.com/singnet) - A decentralized marketplace for AI services where agents can buy and sell algorithms.
- [Ocean Protocol](https://github.com/oceanprotocol) - A decentralized data exchange protocol that enables AI agents to access and monetize data.

## Monitoring and Observability

*Tools for monitoring, debugging, and evaluating AI agent performance.*

- [OpenClaw Beacon Scorecard](https://github.com/Scottcjn/beacon-skill) - A liveness and capability scoring system for agents participating in the Beacon discovery network.
- [LangSmith](https://smith.langchain.com/) - LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications and agents.
- [Helicone](https://github.com/Helicone/helicone) - An open-source LLM observability platform for logging, monitoring, and improving AI applications.
- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform with tracing, evaluations, prompt management, and metrics.
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - An open-source AI observability tool for monitoring and evaluating LLM applications in real time.
- [Braintrust](https://www.braintrust.dev/) - An end-to-end platform for evaluating, testing, and shipping AI products with confidence.
- [Weights & Biases](https://github.com/wandb/wandb) - A platform for experiment tracking, model management, and ML pipeline observability.
- [Portkey](https://github.com/Portkey-AI/gateway) - An AI gateway for routing, monitoring, and managing requests across 200+ LLM providers.
- [AgentOps](https://github.com/AgentOps-AI/agentops) - A toolkit for agent monitoring, testing, and replay debugging with session recordings.

## SDKs and Libraries

*Client libraries and SDKs for interacting with agent platforms and services.*

- [bottube](https://pypi.org/project/bottube/) - Python SDK for the BoTTube platform enabling agents to upload videos, post comments, and manage profiles.
- [clawrtc](https://pypi.org/project/clawrtc/) - Python CLI and library for RustChain mining, wallet management, and Coinbase wallet integration.
- [beacon-skill](https://github.com/Scottcjn/beacon-skill) - A Python package for agents to join the OpenClaw Beacon discovery network and broadcast liveness pings.
- [grazer-skill](https://pypi.org/project/grazer-skill/) - A multi-platform social SDK allowing agents to post and interact across BoTTube, Moltbook, ClawCities, and 6 more.
- [OpenAI Python](https://github.com/openai/openai-python) - The official Python client library for the OpenAI API including assistants and tool use.
- [Anthropic Python](https://github.com/anthropics/anthropic-sdk-python) - The official Python client for Claude with support for tool use, streaming, and batching.
- [Google GenAI](https://github.com/google/generative-ai-python) - Google's Python SDK for Gemini models with function calling and multi-modal support.
- [Ollama Python](https://github.com/ollama/ollama-python) - A Python library for running and interacting with local LLMs via the Ollama runtime.
- [LiteLLM](https://github.com/BerriAI/litellm) - A unified interface to call 100+ LLM APIs using the OpenAI format with load balancing and spend tracking.
- [Marvin](https://github.com/prefecthq/marvin) - A lightweight AI engineering toolkit for building natural language interfaces and AI functions.

## Standards and Specifications

*Formal specifications, protocol definitions, and standard documents for the agent ecosystem.*

- [RIP-200](https://github.com/Scottcjn/Rustchain) - RustChain Improvement Proposal for Round-Robin 1-CPU-1-Vote consensus with hardware attestation and time-aged antiquity multipliers.
- [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) - The industry-standard specification for describing HTTP APIs, widely used for agent tool definitions.
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) - A stateless, lightweight remote procedure call protocol used by MCP and other agent communication layers.
- [A2A Protocol Spec](https://github.com/google/A2A) - Google's specification for agent interoperability defining Agent Cards, task lifecycle, and streaming.
- [MCP Specification](https://spec.modelcontextprotocol.io/) - Anthropic's specification for the Model Context Protocol defining tools, resources, and prompts.
- [Tool Use Schemas](https://json-schema.org/) - JSON Schema, the foundation for defining tool parameter schemas across all major agent frameworks.
- [OAuth 2.0](https://oauth.net/2/) - The authorization framework underpinning secure agent-to-service authentication across the ecosystem.
- [WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455) - The full-duplex communication protocol used by many real-time agent streaming implementations.

## Research and Papers

*Academic papers, surveys, and foundational research on AI agents.*

- [A Survey on Large Language Model Based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Comprehensive survey covering LLM-based agent architectures, capabilities, and evaluation (2023).
- [The Rise and Potential of Large Language Model Based Agents](https://arxiv.org/abs/2309.07864) - A survey mapping the conceptual framework for LLM agents from a cognitive science perspective (2023).
- [AgentBench](https://github.com/THUDM/AgentBench) - A benchmark for evaluating LLMs as agents across 8 distinct environments including web, code, and games.
- [Voyager](https://github.com/MineDojo/Voyager) - An LLM-powered lifelong learning agent that explores, acquires skills, and makes discoveries in Minecraft.
- [Generative Agents](https://arxiv.org/abs/2304.03442) - Stanford and Google's research on believable simulacra of human behavior using LLM-driven agents (2023).
- [Toolformer](https://arxiv.org/abs/2302.04761) - Meta's research on language models that learn to use external tools through self-supervised training (2023).
- [ReAct](https://arxiv.org/abs/2210.03629) - The foundational paper on synergizing reasoning and acting in language models for agent task solving (2022).
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) - Google's paper showing that prompting LLMs with intermediate reasoning steps improves complex task performance (2022).
- [MRKL Systems](https://arxiv.org/abs/2205.00445) - A modular neuro-symbolic architecture for combining LLMs with discrete expert modules and tools (2022).
- [Reflexion](https://arxiv.org/abs/2303.11366) - A framework for reinforcing language agents through linguistic feedback and self-reflection (2023).
- [Language Agent Tree Search](https://arxiv.org/abs/2310.04406) - A general framework unifying reasoning, acting, and planning in language agents via Monte Carlo tree search (2023).
- [POWER8 Non-Bijunctive Collapse](https://github.com/Scottcjn/ram-coffers) - Research on vec_perm-based attention collapse and neuromorphic NUMA routing for hardware-native Hebbian inference.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Scottcjn](https://github.com/Scottcjn) has waived all copyright and related or neighboring rights to this work.
