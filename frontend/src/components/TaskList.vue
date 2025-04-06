<template>
    <div class="table-responsive mt-4">
      <table class="table table-bordered">
        <thead class="table-light">
          <tr>
            <th>Task</th>
            <th>Assigned To</th>
            <th>Status</th>
            <th>Deadline</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in tasks" :key="task.id">
            <td>{{ task.title }}</td>
            <td>{{ task.assigned_to }}</td>
            <td>
              <span :class="{
                'badge bg-warning text-dark': task.status === 'Pending',
                'badge bg-success': task.status === 'Completed'
              }">{{ task.status }}</span>
            </td>
            <td>{{ formatDate(task.deadline) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  const props = defineProps(['tasks']);
  
  const formatDate = (dateStr) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString();
  };
  </script>
  