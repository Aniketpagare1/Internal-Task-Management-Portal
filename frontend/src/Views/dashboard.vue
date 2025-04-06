<template>
    <div class="container mt-4">
      <h2>Welcome to the Dashboard</h2>
  
      <div class="row mt-4">
        <div class="col-md-6">
          <CalendarView />
        </div>
        <div class="col-md-6">
          <TaskStatusToggle />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import CalendarView from '../components/CalendarView.vue';
  import TaskStatusToggle from '../components/TaskStatusToggle.vue';
  </script>
  