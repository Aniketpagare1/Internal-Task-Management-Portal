<template>
    <div class="container mt-4">
      <h3>My Tasks</h3>
  
      <div class="table-responsive mt-3">
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Task</th>
              <th>Status</th>
              <th>Deadline</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="task in tasks" :key="task.id">
              <td>{{ task.title }}</td>
              <td>
                <span :class="{
                  'badge bg-success': task.status === 'Completed',
                  'badge bg-warning text-dark': task.status === 'Pending'
                }">{{ task.status }}</span>
              </td>
              <td>{{ task.deadline }}</td>
              <td>
                <button
                  class="btn btn-sm"
                  :class="task.status === 'Pending' ? 'btn-success' : 'btn-warning'"
                  @click="toggleStatus(task)"
                >
                  Mark as {{ task.status === 'Pending' ? 'Completed' : 'Pending' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import api from '@/services/api';
  
  const tasks = ref([]);
  const token = localStorage.getItem('token');
  
  const fetchTasks = async () => {
    try {
      const res = await api.get('/tasks', {
        headers: { Authorization: `Bearer ${token}` }
      });
      tasks.value = res.data.tasks;
    } catch (err) {
      alert('Could not load tasks');
    }
  };
  
  const toggleStatus = async (task) => {
    try {
      const newStatus = task.status === 'Pending' ? 'Completed' : 'Pending';
      await api.put(`/tasks/${task.id}/status`, { status: newStatus }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      task.status = newStatus;
    } catch (err) {
      alert('Failed to update task status');
    }
  };
  
  onMounted(fetchTasks);
  </script>
  