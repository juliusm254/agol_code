import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import OrderScan from "../views/OrderScan.vue";
import SafetyInspection from "../views/SafetyInspection.vue";
import Safetyform from "../components/Safetyform.vue";
import LabDetails from "../components/LabDetails.vue";
import Login from "../views/Login.vue";
import LabInspection from "../views/LabInspection.vue"
import LabResults from "../views/LabResults.vue"
import LabResultsDetails from "../components/LabResultsDetails.vue"
import LabVent from "../views/LabVent.vue"
import LabVentDetails from "../components/LabVentDetails.vue"
import Loading from "../views/Loading.vue"
import LoadingDetails from "../components/LoadingDetails.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/orderscan",
    name: "OrderScan",
    component: OrderScan,
  },
  {
    path: "/safety-inspection",
    name: "SafetyInspection",
    component: SafetyInspection,
  },
  {
    path: "/safety-checklist/:id",
    name: "Safetyform",
    component: Safetyform,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/lab-inspection",
    name: "LabInspection",
    component: LabInspection,
  },
  {
    path: "/lab-details/:id",
    name: "LabDetails",
    component: LabDetails,
  },
  {
    path: "/lab-results",
    name: "LabResults",
    component: LabResults,
  },
  {
    path: "/lab-results/:id",
    name: "LabResultsDetails",
    component: LabResultsDetails,
  },
  {
    path: "/lab-vent/",
    name: "LabVent",
    component: LabVent,
  },
  {
    path: "/lab-vent/:id",
    name: "LabVentDetails",
    component: LabVentDetails,
  },  
  {
    path: "/loading",
    name: "Loading",
    component: Loading,
  },  
  {
    path: "/loading/:id",
    name: "LoadingDetails",
    component: LoadingDetails,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
