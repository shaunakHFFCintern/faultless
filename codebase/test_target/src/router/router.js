import MfaVerification from '../components/MfaVerification.vue';

const routes = [
  {
    path: '/auth/verify',
    name: 'MfaVerify',
    component: MfaVerification,
    meta: { requireEnterprise: true }
  }
];

export default routes;
