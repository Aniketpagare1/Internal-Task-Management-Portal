<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-4">
          <h3 class="text-center mb-4">Employee Login</h3>
          <form @submit.prevent="handleLogin">
            <div class="mb-3">
              <label>Email</label>
              <input v-model="email" type="email" class="form-control" required />
            </div>
            <div class="mb-3">
              <label>Password</label>
              <input v-model="password" type="password" class="form-control" required />
            </div>
            <button class="btn btn-primary w-100" type="submit">Login</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import api from '@/services/api';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const email = ref('');
  const password = ref('');
  
  const handleLogin = async () => {
    try {
      const res = await api.post('/login', {
        email: email.value,
        password: password.value,
      });
      localStorage.setItem('token', res.data.token);
      localStorage.setItem('user', JSON.stringify(res.data.user));
      router.push('/dashboard');
    } catch (err) {
      alert('Invalid credentials');
    }
  };
  </script>
  