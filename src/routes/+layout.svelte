<script>
	import '../app.postcss';
	import { AppShell } from '@skeletonlabs/skeleton';
	import Header from './Header.svelte';

	import './styles.css';
	import Sidebar from '$lib/components/Sidebar.svelte';
</script>

<AppShell>
	<svelte:fragment slot="sidebarLeft">
		<Sidebar />
	</svelte:fragment>
	<slot />
</AppShell>

<style>
</style>
