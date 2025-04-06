import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import AssignTask from '../components/AssignTask.vue';
import CalendarView from '../components/CalendarView.vue';
import TaskStatusToggle from '../components/TaskStatusToggle.vue';
import Dashboard from '../views/Dashboard.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/assign-task', component: AssignTask },
  { path: '/calendar', component: CalendarView },
  { path: '/my-tasks', component: TaskStatusToggle },
  { path: '/dashboard', component: Dashboard }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
