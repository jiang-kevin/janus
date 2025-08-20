<script lang="ts">
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<div>
    {#each data.restaurants as r}
        <p>{r.name}</p>
    {/each}
</div>