<template>
    <div>
      <nav class="navbar navbar-expand-lg navbar-light bg-light px-4">
        <router-link class="navbar-brand" to="/dashboard">Task Manager</router-link>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><router-link class="nav-link" to="/assign-task">Assign Task</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/my-tasks">My Tasks</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/calendar">Calendar</router-link></li>
            <li class="nav-item"><router-link class="nav-link" to="/login">Logout</router-link></li>
          </ul>
        </div>
      </nav>
  
      <router-view />
    </div>
  </template>
  