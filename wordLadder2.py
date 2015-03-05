class sol():
		alphabet = set('abcdefghijklmnopqrstuvwxyz')

		def findLadders(self, start, end, dict):
			dict.add(end)
			level_tracker = collections.defaultdict(set)
			self.parents_tracker = {}
			last = {start}
			while last and end not in level_tracker:
				current = set([])
				level_tracker.clear()
				for word in last:
					for next_word in self.ladder(word, dict):
						if next_word not in self.parents_tracker:
							current.add(next_word)
							level_tracker[next_word].add(word)
				self.parents_tracker.update(level_tracker)
				last = current
			return [] if not last else self.generate_paths(start, end)

		def ladder(self, word, dict):
			for i in xrange(len(word)):
				for letter in self.alphabet - {word[i]}:
					new_word = word[:i] + letter + word[i + 1:]
					if new_word in dict:
						yield new_word

		def generate_paths(self, start, end):
			ret = [[end]]
			while ret[-1][0] != start:
				new_ret = []
				for path in ret:
					for parent in self.parents_tracker[path[0]]:
						new_ret.append([parent] + path)
				ret = new_ret
			return ret
a=sol()
"hot","dot","dog","lot","log"]
a.findLadders("sam","bad",)