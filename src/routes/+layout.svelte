<script>
	import '../app.postcss';
	import { AppShell } from '@skeletonlabs/skeleton';
	import { computePosition, autoUpdate, offset, shift, flip, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';

	import './styles.css';
	import Sidebar from '$lib/components/Sidebar.svelte';

	export let data;
	storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });
</script>

<AppShell>
	<svelte:fragment slot="sidebarLeft">
		<Sidebar {data} />
	</svelte:fragment>
	<slot />
</AppShell>

<style>
</style>
