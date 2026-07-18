# Hi, I'm Allen 👋

<a href="https://haiiibin.github.io"><img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=19&pause=1100&color=2A78D6&width=560&lines=Data+%26+AI+Analyst;I+build+AI+agent+workflows+with+Claude+Code;Forecasting+%C2%B7+Optimization+%C2%B7+Machine+Learning" alt="Typing intro"/></a>

**Data & AI Analyst | UBC MBAN | Forecasting · Optimization · ML**

I build AI agent workflows and data products: two MCP servers published on PyPI (a tabular-data profiler and a Canadian capital-gains engine), a multi-agent investing framework where Buffett, Munger, and Burry personas debate my portfolio, and the forecasting, optimization, and machine learning work below. Claude Code and MCP are built into how I work every day.

## 🔭 Now

- Just shipped [data-profiler-mcp](https://github.com/haiiibin/data-profiler-mcp) and [acb-tax-mcp](https://github.com/haiiibin/acb-tax-mcp) to PyPI: install with `pip`, CI-tested, submitted to awesome-mcp-servers
- Building [claude-multi-agent-investing](https://github.com/haiiibin/claude-multi-agent-investing): teaching 12 agents to argue about my portfolio so I don't have to
- Contributing fixes upstream to the tools I depend on: PuLP, sec-edgar-mcp, yahoo-finance-mcp (see Open Source below)

## 📌 Featured Projects

### 🤖 Open Source & AI Agents

#### [Claude Multi-Agent Investing](https://github.com/haiiibin/claude-multi-agent-investing)

12 agents (Buffett, Munger, and Burry personas, 6 fact-gathering analysts, 1 portfolio-manager synthesizer) debate every holding through 13 slash commands: tax-aware for Canadian accounts, advisory only, zero API cost beyond a Claude Code subscription.

<img src="./images/investing_agents.png" alt="Multi-agent investing architecture" width="560"/>

#### [data-profiler-mcp](https://github.com/haiiibin/data-profiler-mcp) · on [PyPI](https://pypi.org/project/data-profiler-mcp/)

MCP server that lets an LLM understand any tabular data file (CSV, Parquet, Excel, JSON): schema, per-column statistics, severity-ranked data-quality flags, and memory-saving dtype suggestions. `pip install data-profiler-mcp`, CI-tested on Python 3.10 to 3.12.

<img src="https://raw.githubusercontent.com/haiiibin/data-profiler-mcp/main/docs/demo.gif" alt="data-profiler-mcp demo" width="560"/>

#### [acb-tax-mcp](https://github.com/haiiibin/acb-tax-mcp) · on [PyPI](https://pypi.org/project/acb-tax-mcp/)

Canadian adjusted cost base and capital gains for LLM agents: CRA average-cost method, per-disposition realized gains, and superficial-loss detection with the denied loss deferred into the substitute shares' ACB. Decimal-precise to the cent, zero heavy dependencies, a calculation aid (not tax advice).

### 📈 Analytics & ML

#### [YVR Energy Consumption Forecasting](https://github.com/haiiibin/Vancouver-International-Airport-Energy-Consumption-Forecasting)

Forecasting 14 years of monthly energy consumption for Vancouver International Airport with Box-Cox transformation and seasonal ARIMA: **1.7% MAPE** on holdout data, with 3-year projections supporting procurement planning.

<img src="./images/yvr_forecast.png" alt="YVR forecast" width="500"/>

#### [Machine Learning for Diabetes Risk Screening](https://github.com/haiiibin/Machine-Learning-for-Diabetes-Risk-Screening)

Two-stage ML pipeline (logistic regression screening, then random forest diagnosis) that cuts unnecessary lab tests by **30%** while keeping **95% detection sensitivity** (F1 = 0.87).

<img src="./images/diabetes_results.png" alt="Diabetes model results" width="500"/>

#### [School Bus Route Optimization](https://github.com/haiiibin/school-bus-route-optimization)

Mixed-integer linear programming model reassigning 2,000 students after a school closure: base solution **$1.73M/year with 29 buses**, plus a weather-constrained scenario quantifying the safety vs. cost trade-off.

<img src="./images/schoolbus_result.png" alt="School bus optimization results" width="500"/>

**More projects:** [US stock price prediction (VAR / LASSO / LSTM)](https://github.com/haiiibin/us-stock-price-prediction) · [10-K NLP industry analysis](https://github.com/haiiibin/health-service-industry-analysis) · [TikTok reviews sentiment analysis (Python + R)](https://github.com/haiiibin/tiktok-reviews-sentiment-analysis) · [Nutrition planning optimization (LP)](https://github.com/haiiibin/nutrition-planning-optimization)

## 🔧 Open Source Contributions

Besides maintaining [data-profiler-mcp](https://github.com/haiiibin/data-profiler-mcp) and [acb-tax-mcp](https://github.com/haiiibin/acb-tax-mcp) (both on PyPI), I contribute fixes upstream to the tools I depend on:

- [coin-or/pulp #936](https://github.com/coin-or/pulp/pull/936) expose CBC's `randomSeed` on `COIN_CMD` for reproducible MILP solves (under review)
- [sec-edgar-mcp #142](https://github.com/stefanoamorelli/sec-edgar-mcp/pull/142) fix 9 tools whose descriptions were silently empty (f-string docstrings never reach `__doc__`), with a regression test (under review)
- [yahoo-finance-mcp #16](https://github.com/Alex2Yang97/yahoo-finance-mcp/pull/16) start/end date-range support for historical prices (closes an open issue)
- [yahoo-finance-mcp #17](https://github.com/Alex2Yang97/yahoo-finance-mcp/pull/17) US class-share ticker normalization, so `BRK.B` stops silently returning empty data

## 🛠 Tech Stack

<img src="https://skillicons.dev/icons?i=python,r,mysql,postgres,mongodb,sklearn,pytorch,tensorflow,aws,gcp,azure,git&perline=12" alt="Tech stack icons"/>

- **Languages & Data:** Python, R, SQL (PostgreSQL, BigQuery), Pandas, scikit-learn, PyTorch
- **Modeling:** time series forecasting, optimization (MILP / LP), statistical inference, ML pipelines
- **BI & Visualization:** Power BI, Tableau, Looker Studio, advanced Excel
- **AI & Developer Tools:** Claude Code (MCP, CLI, API), GitHub Copilot, prompt engineering, AI workflow automation

## 📊 GitHub Stats

<img src="https://streak-stats.demolab.com?user=haiiibin&hide_border=true&background=FFFFFF00&ring=2A78D6&fire=2A78D6&currStreakLabel=2A78D6" alt="GitHub streak" height="160"/>

## ⚡ Recent Activity

<!-- Auto-updated daily by .github/workflows/update-readme.yml -->
<!--RECENT_ACTIVITY:start-->
- `2026-07-18` Opened PR in [unit8co/darts](https://github.com/unit8co/darts)
- `2026-07-11` Opened PR in [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- `2026-07-10` Opened PR in [coin-or/pulp](https://github.com/coin-or/pulp)
- `2026-07-10` Opened PR in [stefanoamorelli/sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)
- `2026-07-18` Pushed 1 commit to [haiiibin/darts](https://github.com/haiiibin/darts)
<!--RECENT_ACTIVITY:end-->

## 🎓 Education & Certifications

- **Master of Business Analytics (MBAN)**, UBC Sauder School of Business (Nov 2025)
- **BA in Economics**, Minor in Commerce, UBC (May 2024), graduated with distinction
- **CFA Level II Candidate**

## 📫 Contact

Happy to talk AI-agent tooling or analytics work. Reach me here:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-haiiibin-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haiiibin)
[![Email](https://img.shields.io/badge/Email-haibiny123%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:haibiny123@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-haiiibin.github.io-2A78D6)](https://haiiibin.github.io)
