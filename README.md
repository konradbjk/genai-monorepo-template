# GenAI Monorepo Template

This library was created

**Stack**:

- nx
- nextjs
- langflow
- n8n
- ollama
- qdrant
- mongodb
- postgres
- fastapi

## Prerequisite

Download [Visual Studio Code](https://code.visualstudio.com/) compatible with your operating system.

### Install Nx Console

Nx Console is an editor extension that enriches your developer experience. It lets you run tasks, generate code, and improves code autocompletion in your IDE. It is available for VSCode and IntelliJ.

[Install Nx Console &raquo;](https://nx.dev/getting-started/editor-setup?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

## Disclaimer

Repo was built on top of the default `create-nx-workspace`
Command that was run

```bash
npx create-nx-workspace@latest genai-monorepo-template --pm pnpm --preset next --nextAppDir true --nextSrcDir false --workspaceType package-based --e2eTestRunner none --style tailwind
```

## Run tasks

To run the dev server for your app, use:

```sh
npx nx dev genai-monorepo-template
```

To create a production bundle:

```sh
npx nx build genai-monorepo-template
```

To see all available targets to run for a project, run:

```sh
npx nx show project genai-monorepo-template
```

These targets are either [inferred automatically](https://nx.dev/concepts/inferred-tasks?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) or defined in the `project.json` or `package.json` files.

[More about running tasks in the docs &raquo;](https://nx.dev/features/run-tasks?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

## Add new projects

While you could add new projects to your workspace manually, you might want to leverage [Nx plugins](https://nx.dev/concepts/nx-plugins?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) and their [code generation](https://nx.dev/features/generate-code?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) feature.

Use the plugin's generator to create new projects.

To generate a new application, use:

```sh
npx nx g @nx/next:app demo
```

To generate a new library, use:

```sh
pnpm nx g  @nx/next:lib  ui --importPath=@packages/ui --bundler=vite
```
