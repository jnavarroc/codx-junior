{"name": "store_module", "description": "Guidelines for developing and maintaining store modules.", "category": "file", "file_match": "\\/store\\/", "content": "import { getterTree, mutationTree, actionTree } from 'typed-vuex'\nimport store, { $storex } from '.'\nimport { API } from '../api/api'\n\nexport const namespaced = true\n\nexport const state = () => ({\n  allProjects: null,\n  chats: null,\n  activeChat: null,\n  activeProject: null,\n  logs: null,\n  formatedLogs: [],\n  selectedLog: null,\n  autoRefresh: false\n})\n\nexport const mutations = mutationTree(state, {\n  setAllProjects(state, allProjects) {\n    state.allProjects = allProjects\n    state.activeChat = null\n  },\n  setLogs(state, logs) {\n    state.logs = logs\n  },\n  setFormatedLogs(state, formatedLogs) {\n    state.formatedLogs = formatedLogs\n  }\n})\n\nexport const getters = getterTree(state, {\n  allTags: state => new Set(state.chats?.map(c => c.tags).reduce((a, b) => a.concat(b), []) || []),\n  projectDependencies: state => {\n    const { project_dependencies } = state.activeProject\n    return project_dependencies?.split(\",\")\n        .map(project_name => state.allProjects\n        .find(p => p.project_name === project_name))\n        .filter(f => !!f)\n  },\n  childProjects: state => {\n    const { _sub_projects } = state.activeProject\n    return _sub_projects?.map(project_name => state.allProjects\n        .find(p => p.project_name === project_name))\n        .filter(f => !!f)\n  },\n  projectHierarchy: (state) => {\n    const hierarchy = state.allProjects.map(project => ({ ...project }))\n    return hierarchy.map(project => {\n      project.parent_project = hierarchy\n                        .filter(pp => project.project_path != pp.project_path) \n                        .find(pp => project.project_path.startsWith(pp.project_path))\n      project.sub_projects = hierarchy\n                        .filter(pp => project.project_path != pp.project_path)\n                        .filter(pp => pp.project_path.startsWith(project.project_path))\n      return project\n    })\n  }\n})\n\nexport const actions = actionTree(\n  { state, getters, mutations },\n  {\n    async init () {\n      await $storex.projects.loadAllProjects()\n    },\n    async loadAllProjects() {\n      await API.project.list()\n      $storex.projects.setAllProjects(API.allProjects)\n      $storex.projects.setActiveProject(API.lastSettings)\n    },\n    async setActiveProject ({ state }, project) {\n      if (project?.codx_path === state.activeProject?.codx_path) {\n        return\n      }\n      await API.init(project?.codx_path)\n      state.activeProject = API.lastSettings\n      state.activeChat = null\n      project && await $storex.projects.loadChats()\n    },\n", "path": "/shared/codx-junior/client/.codx/profiles/store_module.profile"}