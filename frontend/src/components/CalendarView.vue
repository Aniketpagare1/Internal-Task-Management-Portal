<template>
    <div class="container mt-4">
      <h3 class="mb-4">Task Deadlines Calendar</h3>
      <FullCalendar
        :plugins="calendarPlugins"
        :events="taskEvents"
        :initialView="'dayGridMonth'"
      />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import FullCalendar from '@fullcalendar/vue3';
  import dayGridPlugin from '@fullcalendar/daygrid';
  import api from '@/services/api';
  
  const calendarPlugins = [dayGridPlugin];
  const taskEvents = ref([]);
  const token = localStorage.getItem('token');
  
  const loadEvents = async () => {
    try {
      const res = await api.get('/tasks', {
        headers: { Authorization: `Bearer ${token}` }
      });
  
      taskEvents.value = res.data.tasks.map((task) => ({
        title: task.title,
        date: task.deadline,
      }));
    } catch (err) {
      console.error(err);
      alert('Failed to load calendar data.');
    }
  };
  
  onMounted(loadEvents);
  </script>
  