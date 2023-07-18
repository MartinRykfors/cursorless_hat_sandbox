build_dir : build
	mkdir build

.PHONY : build
build : | build_dir
	find svgs -name '*.svg' -printf "%f\n" | xargs -I{} scour -i svgs/{} -o build/{} --remove-metadata

.PHONY : clean
clean :
	rm -r build && rm preview.html

.PHONY : preview
preview :
	python generate_preview.py

.PHONY : serve
serve : preview
	python -m http.server 8000
