<template>
    <div class="container mt-4">
      <h2>Welcome, {{ user.name }}</h2>
      <p>Role: <strong>{{ user.role }}</strong></p>
  
      <div v-if="user.role === 'manager'" class="my-3">
        <router-link to="/assign-task" class="btn btn-success">Assign New Task</router-link>
      </div>
  
      <TaskList :tasks="tasks" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import api from '@/services/api';
  import TaskList from '@/components/TaskList.vue';
  
  const user = JSON.parse(localStorage.getItem('user'));
  const tasks = ref([]);
  
  const fetchTasks = async () => {
    try {
      const token = localStorage.getItem('token');
      const res = await api.get('/tasks', {
        headers: { Authorization: `Bearer ${token}` }
      });
      tasks.value = res.data.tasks;
    } catch (err) {
      console.error(err);
      alert('Failed to fetch tasks.');
    }
  };
  
  onMounted(fetchTasks);
  </script>
  