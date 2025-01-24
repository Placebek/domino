<template>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 150" :class="customClass">
    <!-- Domino pieces -->
    <rect id="domino1" x="30" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
      <animateTransform
        attributeName="transform"
        type="rotate"
        begin="0s"
        dur="4s"
        keyTimes="0; 0.5; 1"
        values="0 40 60; 90 40 60; 90 40 60"
        fill="freeze"
        repeatCount="indefinite"
      />
    </rect>
    <rect id="domino2" x="60" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
      <animateTransform
        attributeName="transform"
        type="rotate"
        begin="0s"
        dur="4s"
        keyTimes="0; 0.125; 0.525; 1"
        values="0 70 60;0 70 60; 90 70 60; 90 70 60"
        from="0 70 60"
        to="90 70 60"
        fill="freeze"
        repeatCount="indefinite"
      />
    </rect>
    <rect id="domino3" x="90" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
      <animateTransform
        attributeName="transform"
        type="rotate"
        begin="0s"
        dur="4s"
        keyTimes="0; 0.25; 0.65; 1"
        values="0 100 60;0 100 60; 90 100 60; 90 100 60"
        from="0 100 60"
        to="90 100 60"
        fill="freeze"
        repeatCount="indefinite"
      />
    </rect>
    <rect id="domino4" x="120" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
      <animateTransform
        attributeName="transform"
        type="rotate"
        begin="0s"
        dur="4s"
        keyTimes="0; 0.375; 0.775; 1"
        values="0 130 60;0 130 60; 90 130 60; 90 130 60"
        from="0 130 60"
        to="90 130 60"
        fill="freeze"
        repeatCount="indefinite"
      />
    </rect>
    <rect id="domino5" x="150" y="30" width="20" height="60" fill="#4497D5" rx="3" ry="3">
      <animateTransform
        attributeName="transform"
        type="rotate"
        begin="0s"
        dur="4s"
        keyTimes="0; 0.5; 0.9; 1"
        values="0 160 60; 0 160 60; 90 160 60; 90 160 60"
        from="0 160 60"
        to="90 160 60"
        fill="freeze"
        repeatCount="indefinite"
      />
    </rect>
  </svg>
</template>

<script>
export default {
  name: 'FallDominoAnimate',
  props: {
    customClass: {
      type: String,
      default: '',
    },
  },
}
</script>
