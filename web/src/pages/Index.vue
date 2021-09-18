<template>
  <q-page class="flex flex-center">
    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <q-input
        filled
        v-model="formData.username"
        label="用户名"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || '请输入用户名']"
      />

      <q-input
        filled
        type="password"
        v-model="formData.password"
        label="密码"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || '请输入密码']"
      />

      <q-input
        filled
        type="number"
        v-model="formData.step"
        label="步数"
        lazy-rules
        :rules="[
          (val) => (val) => (val !== null && val !== '') || '请输入步数',
        ]"
      />

      <div>
        <q-btn label="提交" type="submit" color="primary" />
        <q-btn label="重置" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </q-form>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { SetStep } from "src/api/mimotion";
import { useQuasar } from "quasar";
export default defineComponent({
  name: "PageIndex",
  setup(props, context) {
    const $q = useQuasar();
    const formData = ref({
      username: "",
      password: "",
      step: 20000,
    });
    const onSubmit = async () => {
      $q.loading.show();
      const form = formData.value;
      try {
        const result = await SetStep(form.username, form.password, form.step);
        if (result) {
          if (result.data.code === 0) {
            $q.notify({
              message: result.data.message,
              position: "center",
              timeout: 2000,
              icon: "done",
              color: "green",
            });
          } else {
            $q.notify({
              message: result.data.message,
              position: "center",
              timeout: 2000,
              icon: "info",
              color: "red",
            });
          }
        }
      } catch {
        $q.notify({
          message: "请求错误",
          position: "center",
          timeout: 2000,
          icon: "info",
          color: "red",
        });
      } finally {
        $q.loading.hide();
      }
    };
    const onReset = () => {
      formData.value.username = "";
      formData.value.password = "";
      formData.value.step = 20000;
    };
    return {
      onSubmit,
      onReset,
      formData,
    };
  },
});
</script>
