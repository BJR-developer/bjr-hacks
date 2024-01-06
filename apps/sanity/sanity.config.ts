import { defineConfig } from "sanity";
import { deskTool } from "sanity/desk";
import { visionTool } from "@sanity/vision";
import { colorInput } from "@sanity/color-input";
import { schemaTypes } from "./schemas";

export default defineConfig({
	name: "default",
	title: "hackers",

	projectId: "jz2np8nm",
	dataset: "production",

	plugins: [deskTool(), visionTool(), colorInput()],

	schema: {
		types: schemaTypes,
	},
});
