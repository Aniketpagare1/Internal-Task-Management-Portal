<template>
    <div class="container mt-4">
      <h3 class="mb-4">Assign a New Task</h3>
  
      <form @submit.prevent="assignTask">
        <div class="mb-3">
          <label class="form-label">Task Title</label>
          <input v-model="form.title" type="text" class="form-control" required />
        </div>
  
        <div class="mb-3">
          <label class="form-label">Description</label>
          <textarea v-model="form.description" class="form-control" rows="3" required></textarea>
        </div>
  
        <div class="mb-3">
          <label class="form-label">Assign To</label>
          <select v-model="form.assigned_to" class="form-select" required>
            <option value="" disabled>Select an employee</option>
            <option v-for="emp in employees" :key="emp.id" :value="emp.id">
              {{ emp.name }} ({{ emp.email }})
            </option>
          </select>
        </div>
  
        <div class="mb-3">
          <label class="form-label">Deadline</label>
          <input v-model="form.deadline" type="date" class="form-control" required />
        </div>
  
        <button type="submit" class="btn btn-primary">Assign Task</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import api from '@/services/api';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const form = ref({
    title: '',
    description: '',
    assigned_to: '',
    deadline: ''
  });
  
  const employees = ref([]);
  const token = localStorage.getItem('token');
  
  // Fetch list of employees from backend
  const fetchEmployees = async () => {
    try {
      const res = await api.get('/users/employees', {
        headers: { Authorization: `Bearer ${token}` }
      });
      employees.value = res.data.employees;
    } catch (err) {
      console.error(err);
      alert('Could not fetch employee list');
    }
  };
  
  // Submit form
  const assignTask = async () => {
    try {
      await api.post('/tasks', form.value, {
        headers: { Authorization: `Bearer ${token}` }
      });
      alert('Task assigned successfully!');
      router.push('/dashboard');
    } catch (err) {
      console.error(err);
      alert('Failed to assign task.');
    }
  };
  
  onMounted(fetchEmployees);
  </script>
  