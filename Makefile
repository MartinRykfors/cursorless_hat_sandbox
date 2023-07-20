build :
	mkdir build

.PHONY : all
all : build
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

.PHONY : copy
copy : all
	cp -f build/*.svg ${CURSORLESS_DIR}/images/hats/

.PHONY : install
install : copy
	{ \
	set -e ;\
	cd $$CURSORLESS_DIR ;\
	pnpm -F @cursorless/cursorless-vscode preprocess-svg-hats ; \
	pnpm -F cursorless-vscode install-local ; \
	}
